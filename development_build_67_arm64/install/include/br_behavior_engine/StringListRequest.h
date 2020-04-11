// Generated by gencpp from file br_behavior_engine/StringListRequest.msg
// DO NOT EDIT!


#ifndef BR_BEHAVIOR_ENGINE_MESSAGE_STRINGLISTREQUEST_H
#define BR_BEHAVIOR_ENGINE_MESSAGE_STRINGLISTREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace br_behavior_engine
{
template <class ContainerAllocator>
struct StringListRequest_
{
  typedef StringListRequest_<ContainerAllocator> Type;

  StringListRequest_()
    {
    }
  StringListRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::br_behavior_engine::StringListRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::br_behavior_engine::StringListRequest_<ContainerAllocator> const> ConstPtr;

}; // struct StringListRequest_

typedef ::br_behavior_engine::StringListRequest_<std::allocator<void> > StringListRequest;

typedef boost::shared_ptr< ::br_behavior_engine::StringListRequest > StringListRequestPtr;
typedef boost::shared_ptr< ::br_behavior_engine::StringListRequest const> StringListRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::br_behavior_engine::StringListRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace br_behavior_engine

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::br_behavior_engine::StringListRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::br_behavior_engine::StringListRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::br_behavior_engine::StringListRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::br_behavior_engine::StringListRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "br_behavior_engine/StringListRequest";
  }

  static const char* value(const ::br_behavior_engine::StringListRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::br_behavior_engine::StringListRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StringListRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::br_behavior_engine::StringListRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::br_behavior_engine::StringListRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // BR_BEHAVIOR_ENGINE_MESSAGE_STRINGLISTREQUEST_H