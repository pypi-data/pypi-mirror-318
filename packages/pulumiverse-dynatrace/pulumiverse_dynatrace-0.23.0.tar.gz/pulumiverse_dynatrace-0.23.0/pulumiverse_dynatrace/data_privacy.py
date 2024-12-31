# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DataPrivacyArgs', 'DataPrivacy']

@pulumi.input_type
class DataPrivacyArgs:
    def __init__(__self__, *,
                 data_collection: pulumi.Input['DataPrivacyDataCollectionArgs'],
                 do_not_track: pulumi.Input['DataPrivacyDoNotTrackArgs'],
                 masking: pulumi.Input['DataPrivacyMaskingArgs'],
                 user_tracking: pulumi.Input['DataPrivacyUserTrackingArgs'],
                 application_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataPrivacy resource.
        :param pulumi.Input['DataPrivacyDataCollectionArgs'] data_collection: To provide your end users with the ability to decide for themselves if their activities should be tracked to measure
               application performance and usage, enable opt-in mode.
        :param pulumi.Input['DataPrivacyDoNotTrackArgs'] do_not_track: Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual
               users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.
        :param pulumi.Input['DataPrivacyMaskingArgs'] masking: no documentation available
        :param pulumi.Input['DataPrivacyUserTrackingArgs'] user_tracking: User tracking
        :param pulumi.Input[str] application_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        pulumi.set(__self__, "data_collection", data_collection)
        pulumi.set(__self__, "do_not_track", do_not_track)
        pulumi.set(__self__, "masking", masking)
        pulumi.set(__self__, "user_tracking", user_tracking)
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)

    @property
    @pulumi.getter(name="dataCollection")
    def data_collection(self) -> pulumi.Input['DataPrivacyDataCollectionArgs']:
        """
        To provide your end users with the ability to decide for themselves if their activities should be tracked to measure
        application performance and usage, enable opt-in mode.
        """
        return pulumi.get(self, "data_collection")

    @data_collection.setter
    def data_collection(self, value: pulumi.Input['DataPrivacyDataCollectionArgs']):
        pulumi.set(self, "data_collection", value)

    @property
    @pulumi.getter(name="doNotTrack")
    def do_not_track(self) -> pulumi.Input['DataPrivacyDoNotTrackArgs']:
        """
        Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual
        users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.
        """
        return pulumi.get(self, "do_not_track")

    @do_not_track.setter
    def do_not_track(self, value: pulumi.Input['DataPrivacyDoNotTrackArgs']):
        pulumi.set(self, "do_not_track", value)

    @property
    @pulumi.getter
    def masking(self) -> pulumi.Input['DataPrivacyMaskingArgs']:
        """
        no documentation available
        """
        return pulumi.get(self, "masking")

    @masking.setter
    def masking(self, value: pulumi.Input['DataPrivacyMaskingArgs']):
        pulumi.set(self, "masking", value)

    @property
    @pulumi.getter(name="userTracking")
    def user_tracking(self) -> pulumi.Input['DataPrivacyUserTrackingArgs']:
        """
        User tracking
        """
        return pulumi.get(self, "user_tracking")

    @user_tracking.setter
    def user_tracking(self, value: pulumi.Input['DataPrivacyUserTrackingArgs']):
        pulumi.set(self, "user_tracking", value)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)


@pulumi.input_type
class _DataPrivacyState:
    def __init__(__self__, *,
                 application_id: Optional[pulumi.Input[str]] = None,
                 data_collection: Optional[pulumi.Input['DataPrivacyDataCollectionArgs']] = None,
                 do_not_track: Optional[pulumi.Input['DataPrivacyDoNotTrackArgs']] = None,
                 masking: Optional[pulumi.Input['DataPrivacyMaskingArgs']] = None,
                 user_tracking: Optional[pulumi.Input['DataPrivacyUserTrackingArgs']] = None):
        """
        Input properties used for looking up and filtering DataPrivacy resources.
        :param pulumi.Input[str] application_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        :param pulumi.Input['DataPrivacyDataCollectionArgs'] data_collection: To provide your end users with the ability to decide for themselves if their activities should be tracked to measure
               application performance and usage, enable opt-in mode.
        :param pulumi.Input['DataPrivacyDoNotTrackArgs'] do_not_track: Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual
               users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.
        :param pulumi.Input['DataPrivacyMaskingArgs'] masking: no documentation available
        :param pulumi.Input['DataPrivacyUserTrackingArgs'] user_tracking: User tracking
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if data_collection is not None:
            pulumi.set(__self__, "data_collection", data_collection)
        if do_not_track is not None:
            pulumi.set(__self__, "do_not_track", do_not_track)
        if masking is not None:
            pulumi.set(__self__, "masking", masking)
        if user_tracking is not None:
            pulumi.set(__self__, "user_tracking", user_tracking)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="dataCollection")
    def data_collection(self) -> Optional[pulumi.Input['DataPrivacyDataCollectionArgs']]:
        """
        To provide your end users with the ability to decide for themselves if their activities should be tracked to measure
        application performance and usage, enable opt-in mode.
        """
        return pulumi.get(self, "data_collection")

    @data_collection.setter
    def data_collection(self, value: Optional[pulumi.Input['DataPrivacyDataCollectionArgs']]):
        pulumi.set(self, "data_collection", value)

    @property
    @pulumi.getter(name="doNotTrack")
    def do_not_track(self) -> Optional[pulumi.Input['DataPrivacyDoNotTrackArgs']]:
        """
        Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual
        users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.
        """
        return pulumi.get(self, "do_not_track")

    @do_not_track.setter
    def do_not_track(self, value: Optional[pulumi.Input['DataPrivacyDoNotTrackArgs']]):
        pulumi.set(self, "do_not_track", value)

    @property
    @pulumi.getter
    def masking(self) -> Optional[pulumi.Input['DataPrivacyMaskingArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "masking")

    @masking.setter
    def masking(self, value: Optional[pulumi.Input['DataPrivacyMaskingArgs']]):
        pulumi.set(self, "masking", value)

    @property
    @pulumi.getter(name="userTracking")
    def user_tracking(self) -> Optional[pulumi.Input['DataPrivacyUserTrackingArgs']]:
        """
        User tracking
        """
        return pulumi.get(self, "user_tracking")

    @user_tracking.setter
    def user_tracking(self, value: Optional[pulumi.Input['DataPrivacyUserTrackingArgs']]):
        pulumi.set(self, "user_tracking", value)


class DataPrivacy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 data_collection: Optional[pulumi.Input[Union['DataPrivacyDataCollectionArgs', 'DataPrivacyDataCollectionArgsDict']]] = None,
                 do_not_track: Optional[pulumi.Input[Union['DataPrivacyDoNotTrackArgs', 'DataPrivacyDoNotTrackArgsDict']]] = None,
                 masking: Optional[pulumi.Input[Union['DataPrivacyMaskingArgs', 'DataPrivacyMaskingArgsDict']]] = None,
                 user_tracking: Optional[pulumi.Input[Union['DataPrivacyUserTrackingArgs', 'DataPrivacyUserTrackingArgsDict']]] = None,
                 __props__=None):
        """
        Create a DataPrivacy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        :param pulumi.Input[Union['DataPrivacyDataCollectionArgs', 'DataPrivacyDataCollectionArgsDict']] data_collection: To provide your end users with the ability to decide for themselves if their activities should be tracked to measure
               application performance and usage, enable opt-in mode.
        :param pulumi.Input[Union['DataPrivacyDoNotTrackArgs', 'DataPrivacyDoNotTrackArgsDict']] do_not_track: Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual
               users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.
        :param pulumi.Input[Union['DataPrivacyMaskingArgs', 'DataPrivacyMaskingArgsDict']] masking: no documentation available
        :param pulumi.Input[Union['DataPrivacyUserTrackingArgs', 'DataPrivacyUserTrackingArgsDict']] user_tracking: User tracking
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataPrivacyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DataPrivacy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DataPrivacyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataPrivacyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 data_collection: Optional[pulumi.Input[Union['DataPrivacyDataCollectionArgs', 'DataPrivacyDataCollectionArgsDict']]] = None,
                 do_not_track: Optional[pulumi.Input[Union['DataPrivacyDoNotTrackArgs', 'DataPrivacyDoNotTrackArgsDict']]] = None,
                 masking: Optional[pulumi.Input[Union['DataPrivacyMaskingArgs', 'DataPrivacyMaskingArgsDict']]] = None,
                 user_tracking: Optional[pulumi.Input[Union['DataPrivacyUserTrackingArgs', 'DataPrivacyUserTrackingArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataPrivacyArgs.__new__(DataPrivacyArgs)

            __props__.__dict__["application_id"] = application_id
            if data_collection is None and not opts.urn:
                raise TypeError("Missing required property 'data_collection'")
            __props__.__dict__["data_collection"] = data_collection
            if do_not_track is None and not opts.urn:
                raise TypeError("Missing required property 'do_not_track'")
            __props__.__dict__["do_not_track"] = do_not_track
            if masking is None and not opts.urn:
                raise TypeError("Missing required property 'masking'")
            __props__.__dict__["masking"] = masking
            if user_tracking is None and not opts.urn:
                raise TypeError("Missing required property 'user_tracking'")
            __props__.__dict__["user_tracking"] = user_tracking
        super(DataPrivacy, __self__).__init__(
            'dynatrace:index/dataPrivacy:DataPrivacy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            data_collection: Optional[pulumi.Input[Union['DataPrivacyDataCollectionArgs', 'DataPrivacyDataCollectionArgsDict']]] = None,
            do_not_track: Optional[pulumi.Input[Union['DataPrivacyDoNotTrackArgs', 'DataPrivacyDoNotTrackArgsDict']]] = None,
            masking: Optional[pulumi.Input[Union['DataPrivacyMaskingArgs', 'DataPrivacyMaskingArgsDict']]] = None,
            user_tracking: Optional[pulumi.Input[Union['DataPrivacyUserTrackingArgs', 'DataPrivacyUserTrackingArgsDict']]] = None) -> 'DataPrivacy':
        """
        Get an existing DataPrivacy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        :param pulumi.Input[Union['DataPrivacyDataCollectionArgs', 'DataPrivacyDataCollectionArgsDict']] data_collection: To provide your end users with the ability to decide for themselves if their activities should be tracked to measure
               application performance and usage, enable opt-in mode.
        :param pulumi.Input[Union['DataPrivacyDoNotTrackArgs', 'DataPrivacyDoNotTrackArgsDict']] do_not_track: Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual
               users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.
        :param pulumi.Input[Union['DataPrivacyMaskingArgs', 'DataPrivacyMaskingArgsDict']] masking: no documentation available
        :param pulumi.Input[Union['DataPrivacyUserTrackingArgs', 'DataPrivacyUserTrackingArgsDict']] user_tracking: User tracking
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataPrivacyState.__new__(_DataPrivacyState)

        __props__.__dict__["application_id"] = application_id
        __props__.__dict__["data_collection"] = data_collection
        __props__.__dict__["do_not_track"] = do_not_track
        __props__.__dict__["masking"] = masking
        __props__.__dict__["user_tracking"] = user_tracking
        return DataPrivacy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[Optional[str]]:
        """
        The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="dataCollection")
    def data_collection(self) -> pulumi.Output['outputs.DataPrivacyDataCollection']:
        """
        To provide your end users with the ability to decide for themselves if their activities should be tracked to measure
        application performance and usage, enable opt-in mode.
        """
        return pulumi.get(self, "data_collection")

    @property
    @pulumi.getter(name="doNotTrack")
    def do_not_track(self) -> pulumi.Output['outputs.DataPrivacyDoNotTrack']:
        """
        Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual
        users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.
        """
        return pulumi.get(self, "do_not_track")

    @property
    @pulumi.getter
    def masking(self) -> pulumi.Output['outputs.DataPrivacyMasking']:
        """
        no documentation available
        """
        return pulumi.get(self, "masking")

    @property
    @pulumi.getter(name="userTracking")
    def user_tracking(self) -> pulumi.Output['outputs.DataPrivacyUserTracking']:
        """
        User tracking
        """
        return pulumi.get(self, "user_tracking")

