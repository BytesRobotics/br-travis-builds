#!/usr/bin/env python

# author @Alden Parker
# version 3.1
# This is the emotion viewer node. It is what displays and plays the face and sounds that are used to simulate emotions
# in the Garbage Bytes
# for Generative Robotics

from std_msgs.msg import String
from br_behavior_engine.srv import StringList, StringListResponse
from br_behavior_engine.msg import Events
import rospy
from os.path import expanduser
import pyglet
import math
from pyglet.gl import *
import time
import random
import os
import sys
import vlc
import threading
import spotipy
import socket
import requests
from urllib.request import urlopen


# WIFI CHECK FUNCTION
def internet_on():
    try:
        urlopen('http://216.58.192.142', timeout=0.5)
        return True

    except urllib.request.URLError as err:
        return False

    except socket.timeout as e:
        rospy.loginfo("Wifi Check: Socket Timeout")


# Sound List Service
def sound_list_service(req):
    cwd = os.path.dirname(os.path.realpath(__file__)) + "/"

    first_list = os.listdir(cwd + "wav_files")
    final_list = []

    for x in first_list:
        final_list.append(x[:-4])

    return StringListResponse(final_list)


# Face Callback
def face_call(data, progra):
    # Events

    if data.data == "blink_down":
        progra.blink_down()
    elif data.data == "blink_up":
        progra.blink_up()
    elif data.data == "blink_off":
        progra.blink = False
    elif data.data == "blink_on":
        progra.blink = True
    elif data.data == "stats_off":
        progra.tick_choice = False
        progra.fps_choice = False
    elif data.data == "stats_on":
        progra.tick_choice = True
        progra.fps_choice = True
    elif data.data == "happy1":
        if not progra.vid_on:
            progra.happy = True


# Sound Callback
def sound_call(data, progra):
    # Events

    progra.sound = "wav_files/" + data.data


# AI Music Callback
def music_call(data, progra):
    # Events

    if data.data == "random":
        progra.stream_mp3.play_random()
    elif data.data == "list_songs":
        progra.stream_mp3.list_songs()
    elif data.data == "stop_song":
        progra.stream_mp3.stop()
    else:
        progra.stream_mp3.play_song(data.data)


class event_publisher:
    # Event Checker and Publishing

    def __init__(self):
        self.old_vid = False
        self.wifi_state = False
        self.wifi_time = time.time()
        self.wifi_change = False

    def checker(self, prog, e_pub):

        while not rospy.is_shutdown():
            if prog.vid_on != self.old_vid or self.wifi_change:
                msg = Events()
                msg.wifi = prog.wifi
                msg.video = prog.vid_on
                self.old_vid = prog.vid_on
                self.wifi_state = prog.wifi

                e_pub.publish(msg)

                if self.wifi_change:
                    self.wifi_change = False

            if (time.time() - self.wifi_time) >= 5:
                self.wifi_time = time.time()
                if not internet_on():
                    prog.wifi = False
                    if self.wifi_state is not False:
                        self.wifi_state = False
                        self.wifi_change = True
                else:
                    prog.wifi = True
                    if self.wifi_state is not True:
                        self.wifi_state = True
                        self.wifi_change = True

            time.sleep(0.1)


class eyes:
    # Class for eyes

    def __init__(self, eye1, eye2):
        self.eye1 = eye1  # Actual pyglet object
        self.eye2 = eye2


class clock:

    def __init__(self, fr):
        self.start_time = time.time()
        self.tick = 0
        self.tick_rate = 1 / fr

    def get_fps(self):
        time_diff = time.time() - self.start_time
        fps_num = self.tick // time_diff

        return fps_num

    def get_tick(self):
        return self.tick

    def tick_inc(self):
        self.tick += 1
        time.sleep(self.tick_rate)


class program:

    def __init__(self, fr, tick, fps, bs):
        self.cwd = os.path.dirname(os.path.realpath(__file__)) + "/"

        self.tick_choice = tick  # Get config for tick
        self.fps_choice = fps  # Get config for fps

        self.clock = clock(fr)  # Start clock

        # IA Song Stream
        self.stream_mp3 = stream_mp3()

        # Sound
        self.sound_player = pyglet.media.Player()

        # Video
        self.vid_on = False
        self.player = pyglet.media.Player()
        self.source = pyglet.media.StreamingSource()

        # Vert Eyes
        self.vert = vertex()  # Create vertexes
        self.draw_eyes = True
        self.vert.make_eyes(win_width / 2, win_height / 2, 160, 190)
        self.blink_count = bs
        self.blink_speed = bs
        self.blink = True

        # Event Triggers
        self.happy = False
        self.sound = None

        # Wifi
        no_wifi_img = pyglet.image.load(self.cwd + 'imgs/no-wifi.png')
        self.no_wifi = pyglet.sprite.Sprite(no_wifi_img, x=win_width - (win_width * 0.15),
                                            y=win_height - (win_height * 0.2))
        self.no_wifi.scale = 0.15

        self.wifi = internet_on()

    def update(self, dt):
        win.clear()

        if rospy.is_shutdown():
            sys.exit()

        if not self.wifi:
            self.no_wifi.draw()

        # Vert Draw
        if not self.vid_on and self.draw_eyes:
            self.vert.draw()  # Draw non-videos

        if self.tick_choice:

            tic = self.clock.get_tick()
            tick = pyglet.text.Label(str(tic),
                                     font_name='Times New Roman',
                                     font_size=10, x=20, y=20,
                                     anchor_x='center',
                                     anchor_y='center')
            tick.draw()

        if self.fps_choice:

            fps_num = self.clock.get_fps()
            fps = pyglet.text.Label(str(fps_num),
                                    font_name='Times New Roman',
                                    font_size=10, x=20, y=10,
                                    anchor_x='center',
                                    anchor_y='center')
            fps.draw()  # Draw FPS

        self.event_handler(self.clock.get_tick())

        self.clock.tick_inc()

    def event_handler(self, clock_tick):
        # Blink Animation
        if self.blink:
            if 0 == (self.blink_count - clock_tick):
                self.blink_down()

            if 0 == ((self.blink_count - clock_tick) + 10):
                self.blink_up()
                self.blink_count += round(self.blink_speed * (1 + random.random()))

        if clock_tick == 0:
            self.vid_on = True
            animation = pyglet.media.load(self.cwd + 'animations/br-bootup.mp4')
            self.player.queue(animation)
            self.player.play()

        if self.happy:
            self.happy_vid()
            self.happy = False

        if self.sound is not None:
            self.play_sound_file(self.sound)
            self.sound = None

    def happy_vid(self):
        self.vid_on = True
        animation = pyglet.media.load(self.cwd + 'animations/happy1_final.mp4')
        self.player.queue(animation)
        self.player.play()

    def blink_down(self):
        y = self.vert.objs["eyes"]

        #  Transform
        count = 0
        new_verts = []

        for i in y.eye1.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i - (win_height / 2))

            count += 1

        y.eye1.vertices = new_verts

        count = 0
        new_verts = []

        for i in y.eye2.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i - (win_height / 2))

            count += 1

        y.eye2.vertices = new_verts

        #  Scale
        count = 0
        new_verts = []

        for i in y.eye1.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i * 0.01)

            count += 1

        y.eye1.vertices = new_verts

        count = 0
        new_verts = []

        for i in y.eye2.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i * 0.01)

            count += 1

        y.eye2.vertices = new_verts

        #  Transform
        count = 0
        new_verts = []

        for i in y.eye1.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i + (win_height / 2))

            count += 1

        y.eye1.vertices = new_verts

        count = 0
        new_verts = []

        for i in y.eye2.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i + (win_height / 2))

            count += 1

        y.eye2.vertices = new_verts

    def blink_up(self):
        y = self.vert.objs["eyes"]  # Transform
        count = 0
        new_verts = []

        #  Transform
        for i in y.eye1.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i - (win_height / 2))

            count += 1

        y.eye1.vertices = new_verts

        count = 0
        new_verts = []

        for i in y.eye2.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i - (win_height / 2))

            count += 1

        y.eye2.vertices = new_verts

        #  Scale
        count = 0
        new_verts = []

        for i in y.eye1.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i * 100)

            count += 1

        y.eye1.vertices = new_verts

        count = 0
        new_verts = []

        for i in y.eye2.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i * 100)

            count += 1

        y.eye2.vertices = new_verts

        #  Transform
        count = 0
        new_verts = []

        for i in y.eye1.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i + (win_height / 2))

            count += 1

        y.eye1.vertices = new_verts

        count = 0
        new_verts = []

        for i in y.eye2.vertices:
            if (count % 2) == 0:
                new_verts.append(i)
            else:
                new_verts.append(i + (win_height / 2))

            count += 1

        y.eye2.vertices = new_verts

    def play_sound_file(self, name):
        soun = pyglet.media.load(self.cwd + name + ".wav")
        self.sound_player.queue(soun)
        self.sound_player.play()

    def player_stop(self):
        self.player.pause()

    def sound_stop(self):
        self.sound_player.pause()

    def sound_next(self):
        self.sound_player.next_source()


class vertex:

    def __init__(self):
        self.objs = {}  # Objects Dict

    def change_eye_color(self, color):
        eye1 = self.objs["eyes"].eye1
        eye2 = self.objs["eyes"].eye2

        verts = eye1.vertices

        count = 0
        colors = []

        for x in verts:
            if (count % 2) == 0:
                for y in color:
                    colors.append(y)

            count += 1

        eye1.colors = colors
        eye2.colors = colors

    def make_eyes(self, cx, cy, r, w):
        eye1 = self.circle(200, cx - w, cy, r)
        eye2 = self.circle(200, cx + w, cy, r)
        both = eyes(eye1, eye2)

        self.objs["eyes"] = both

    def make_circle(self, cx, cy, r):
        circle = self.circle(200, cx, cy, r)

        count = 0
        for x in self.objs:
            if "circle" in x:
                count += 1

        self.objs["circle_" + str(count)] = circle

    def circle(self, num_points, cx, cy, r):
        # Number of points on side, center x, center y, radius
        circle_color = [52, 235, 155]

        verts = []

        for i in range(num_points):
            angle = math.radians(float(i) / num_points * 360.0)
            x = r * math.cos(angle) + cx
            y = r * math.sin(angle) + cy
            verts += [x, y]

        count = 0
        colors = []

        for x in verts:
            if (count % 2) == 0:
                for y in circle_color:
                    colors.append(y)

            count += 1

        circle = pyglet.graphics.vertex_list(num_points, ('v2f', verts), ('c3B', colors))

        return circle

    def move_obj(self, d, axis, object_name):
        count = 0
        new_verts = []
        for x in self.objs[object_name].vertices:
            if axis == "x":
                if (count % 2) == 0:
                    x += d
                    new_verts.append(x)
                else:
                    new_verts.append(x)

            elif axis == "y":
                if (count % 2) == 0:
                    new_verts.append(x)
                else:
                    x += d
                    new_verts.append(x)
            count += 1

        self.objs[object_name].vertices = new_verts

    def draw(self):
        for x in self.objs:
            if "eyes" in x:
                obj = self.objs[x]
                obj.eye1.draw(GL_POLYGON)  # Draw object
                obj.eye2.draw(GL_POLYGON)  # Draw object


class stream_mp3:

    def __init__(self):
        self.player = vlc.MediaPlayer()
        self.songs = {"Take Me Home, Country Roads": "https://ia800300.us.archive.org/12/items/TakeMeHomeCountryRoad/JohnDenver-TakeMeHomeCountryRoad.mp3",
                      "Bop": "https://ia802809.us.archive.org/29/items/dababyboponbroadwayhiphopmusicalyomp3converter.com/DaBaby_-_BOP_on_Broadway_Hip_Hop_Musical%5BYoMp3Converter.com%5D.mp3",
                      "La La Land": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/Bryce%20Vine%20-%20La%20La%20Land%20ft.%20YG%20%5BOfficial%20Lyric%20Video%5D.mp3",
                      "Highest in the Room": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/Travis%20Scott%20-%20HIGHEST%20IN%20THE%20ROOM%20%28Official%20Music%20Video%29.mp3",
                      "Old Town Road": "https://ia803001.us.archive.org/22/items/oldtownroad/Lil%20Nas%20X%20-%20Old%20Town%20Road%20%28feat.%20Billy%20Ray%20Cyrus%29%20%5BMusic%20Video%5D.mp3",
                      "Never Gonna Give You Up": "https://ia800605.us.archive.org/8/items/NeverGonnaGiveYouUp/jocofullinterview41.mp3",
                      "All Star": "https://ia800306.us.archive.org/16/items/AllStar/SmashMouth-AllStar.mp3",
                      "Fireflies": "https://ia800604.us.archive.org/29/items/OwlCityFireflies/Owl%20City%20-%20Fireflies.mp3",
                      "Sandstorm": "https://ia800701.us.archive.org/15/items/darude_sandstorm_201811/darude_sandstorm.mp3",
                      "Africa": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/Toto%20-%20Africa%20%28Official%20Music%20Video%29.mp3",
                      "Everything is Awesome": "https://ia800901.us.archive.org/21/items/tvtunes_27784/The%20Lego%20Movie%20-%20Everything%20Is%20Awesome.mp3",
                      "Ra Ra Rasputin": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/Ra%20Ra%20Rasputin%20%28Lyrics%29.mp3",
                      "Flying Home": "https://ia801009.us.archive.org/11/items/78_flying-home_lionel-hampton-and-orchestra-lionel-hampton-t-mondello-b-johnson-b-e_gbia0055531a/Flying%20Home%20-%20Lionel%20Hampton%20and%20Orchestra.mp3",
                      "Dance Monkey": "https://ia801506.us.archive.org/33/items/DanceMonkey.flac/Dance%20Monkey.mp3",
                      "Memories": "https://ia801002.us.archive.org/6/items/maroon5memories_201910/Maroon%205%20-%20Memories.mp3",
                      "Circles": "https://ia802805.us.archive.org/30/items/y2mate.compostmalonecircleslyrics0sca9fp6zl8/y2mate.com%20-%20post_malone_circles_lyrics_0sca9FP6zl8.mp3",
                      "Dreamer": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/y2mate.com%20-%20Throttle%20-%20Dreamer%20%5BMonstercat%20Release%5D_K0tYrdTUnxA_320kbps.mp3"}

        self.random_songs = {"Take Me Home, Country Roads": "https://ia800300.us.archive.org/12/items/TakeMeHomeCountryRoad/JohnDenver-TakeMeHomeCountryRoad.mp3",
                             "La La Land": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/Bryce%20Vine%20-%20La%20La%20Land%20ft.%20YG%20%5BOfficial%20Lyric%20Video%5D.mp3",
                             "Old Town Road": "https://ia803001.us.archive.org/22/items/oldtownroad/Lil%20Nas%20X%20-%20Old%20Town%20Road%20%28feat.%20Billy%20Ray%20Cyrus%29%20%5BMusic%20Video%5D.mp3",
                             "Never Gonna Give You Up": "https://ia800605.us.archive.org/8/items/NeverGonnaGiveYouUp/jocofullinterview41.mp3",
                             "All Star": "https://ia800306.us.archive.org/16/items/AllStar/SmashMouth-AllStar.mp3",
                             "Fireflies": "https://ia800604.us.archive.org/29/items/OwlCityFireflies/Owl%20City%20-%20Fireflies.mp3",
                             "Sandstorm": "https://ia800701.us.archive.org/15/items/darude_sandstorm_201811/darude_sandstorm.mp3",
                             "Africa": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/Toto%20-%20Africa%20%28Official%20Music%20Video%29.mp3",
                             "Ra Ra Rasputin": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/Ra%20Ra%20Rasputin%20%28Lyrics%29.mp3",
                             "Dance Monkey": "https://ia801506.us.archive.org/33/items/DanceMonkey.flac/Dance%20Monkey.mp3",
                             "Memories": "https://ia801002.us.archive.org/6/items/maroon5memories_201910/Maroon%205%20-%20Memories.mp3",
                             "Circles": "https://ia802805.us.archive.org/30/items/y2mate.compostmalonecircleslyrics0sca9fp6zl8/y2mate.com%20-%20post_malone_circles_lyrics_0sca9FP6zl8.mp3",
                             "Dreamer": "https://ia601405.us.archive.org/18/items/brycevinelalalandft.ygofficiallyricvideo/y2mate.com%20-%20Throttle%20-%20Dreamer%20%5BMonstercat%20Release%5D_K0tYrdTUnxA_320kbps.mp3"}

    def play_song(self, name):
        self.stop()
        self.player = vlc.MediaPlayer(self.songs[name])
        self.player.play()

    def play_random(self):
        name = random.choice(list(self.random_songs))
        self.stop()
        self.player = vlc.MediaPlayer(self.random_songs[name])
        self.player.play()

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.resume()

    def stop(self):
        self.player.stop()
        self.player.release()
        self.player = None

    def song_list_service(self, req):
        final_list = []

        for x in self.songs:
            final_list.append(x)

        return StringListResponse(final_list)


class spotify_session:

    def __init__(self):
        try:
            client_id = "22abcf8d1c17460f9f6ccac863235adc"
            client_secret = "66be1f9f62ec43bda20b633cd0506e78"
            redirect_uri = "https://garbagebytes.com"
            username = 'ajparker1401'
            scope = 'user-read-private user-read-playback-state user-modify-playback-state'

            self.sp_oauth = spotipy.oauth2.SpotifyOAuth(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
            self.token_info_sp = self.sp_oauth.get_cached_token()

            if not self.token_info_sp:
                auth_url = self.sp_oauth.get_authorize_url()
                print(auth_url)
                response = input('Paste the above link into your browser, then paste the redirect url here: ')

                code = self.sp_oauth.parse_response_code(response)
                self.token_info_sp = self.sp_oauth.get_access_token(code)

            token = self.token_info_sp['access_token']

            self.session = spotipy.Spotify(auth=token)

            self.client_running = False
            self.deviceID = None
            self.tried_on_reconnect = False

            i = 0
            while self.client_running is not True and i != 10:
                devices = self.session.devices()
                for x in devices['devices']:
                    if x["name"] == socket.gethostname():
                        self.deviceID = x['id']
                        self.client_running = True

                i += 1
                time.sleep(1)

            if self.client_running:
                rospy.loginfo("Spotify Client Connected")
            else:
                rospy.logerr("No Spotify Client Running")

        except spotipy.client.SpotifyException as e:
            rospy.logerr("Spotify Server Error:")
            rospy.logerr(e)

        except requests.exceptions.ConnectionError as e:
            rospy.logerr("Wifi Not Connected: Spotify Can't Connect")
            rospy.loginfo(e)

        except Exception as e:
            rospy.logerr(e)

    def refresh_token(self):
        if self.sp_oauth.is_token_expired(self.token_info_sp):
            token_info = self.sp_oauth.refresh_access_token(self.token_info_sp['refresh_token'])
            token = token_info['access_token']
            self.session = spotipy.Spotify(auth=token)

    def play_song(self, name):
        try:
            if self.client_running and internet_on():
                search = self.session.search(name, limit=1, offset=0, type="track", market="US")

                uri = [search["tracks"]["items"][0]["uri"]]

                self.session.start_playback(device_id=self.deviceID, uris=uri)

            elif not self.client_running:
                rospy.logerr("No Spotify Client Running")

            elif not internet_on():
                rospy.logerr("Wifi Not Connected: Spotify Can't Connect")

        except spotipy.client.SpotifyException as e:
            rospy.logerr("Spotify Server Error:")
            rospy.logerr(e)

        except Exception as e:
            rospy.logerr(e)

    def spotify_call(self, data):
        if internet_on() and not self.client_running and not self.tried_on_reconnect:
            i = 0
            while self.client_running is not True and i != 10:
                devices = self.session.devices()
                for x in devices['devices']:
                    if x["name"] == socket.gethostname():
                        self.deviceID = x['id']
                        self.client_running = True

                i += 1
                time.sleep(1)

            if self.client_running:
                rospy.loginfo("Spotify Client Connected")
            else:
                rospy.logerr("No Spotify Client Running")
                self.tried_on_reconnect = True

        if internet_on():
            self.refresh_token()

        if "play" in data.data:
            name = data.data[5:]
            self.play_song(name)


if __name__ == '__main__':
    # Config ----------------------------------------------------------------------------------------------------------
    win_width = 1024  # Width
    win_height = 600  # Height
    clear_color = [0, 0, 0, 1]  # RGBA
    frame_rate = 130.0
    blink_speed = 150
    # -----------------------------------------------------------------------------------------------------------------

    # Create window
    if expanduser("~") == "/home/di3mas":
        win = pyglet.window.Window(width=win_width, height=win_height)  # Create Window
    else:
        win = pyglet.window.Window(width=win_width, height=win_height, fullscreen=True)  # Create Window

    os.system("pactl set-default-sink 'alsa_output.usb-Generic_USB2.0_Device_20130100ph0-00.iec958-stereo'")  # Switch to Speaker
    os.system("pactl set-sink-volume 'alsa_output.usb-Generic_USB2.0_Device_20130100ph0-00.iec958-stereo' 150%")  # Set Volume

    # Set clear color
    pyglet.gl.glClearColor(clear_color[0], clear_color[1], clear_color[2], clear_color[3])  # Set clear color

    # Start Ros stuff
    rospy.init_node('emotion_viewer', anonymous=True)

    # Create program
    prog = program(frame_rate, False, False, blink_speed)

    # Start program with pyglet clock (framerate is number of ticks per second)
    pyglet.clock.schedule_interval(prog.update, 1/frame_rate)

    # Video Drawing
    @win.event
    def on_draw():
        if prog.vid_on:
            try:
                prog.player.get_texture().blit(0, 0, width=win_width, height=win_height)  # Draw frame
            except AttributeError:
                prog.vid_on = False
                prog.player_stop()


    spot = spotify_session()  # Start Spotify

    # Start Subscriber
    rospy.Subscriber("/behavior_engine/face", String, face_call, prog)  # Subscribe to topic
    rospy.Subscriber("/behavior_engine/sounds", String, sound_call, prog)  # Subscribe to topic
    rospy.Subscriber("/behavior_engine/music", String, music_call, prog)  # Subscribe to topic
    rospy.Subscriber("/behavior_engine/spotify", String, spot.spotify_call)  # Subscribe to topic

    sounds = rospy.Service('/behavior_engine/sound_list', StringList, sound_list_service)
    songs = rospy.Service('/behavior_engine/songs_list', StringList, prog.stream_mp3.song_list_service)
    event_pub = rospy.Publisher('/behavior_engine/events', Events, queue_size=3)

    # Start Event Check Thread
    event = event_publisher()
    events_thread = threading.Thread(target=event.checker, args=(prog, event_pub, ))
    events_thread.start()

    # Run App
    pyglet.app.run()  # Run app
