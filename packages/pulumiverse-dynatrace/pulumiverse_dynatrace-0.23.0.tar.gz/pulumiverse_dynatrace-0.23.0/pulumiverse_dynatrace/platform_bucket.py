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

__all__ = ['PlatformBucketArgs', 'PlatformBucket']

@pulumi.input_type
class PlatformBucketArgs:
    def __init__(__self__, *,
                 retention: pulumi.Input[int],
                 table: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PlatformBucket resource.
        :param pulumi.Input[int] retention: The retention of stored data in days
        :param pulumi.Input[str] table: The table the bucket definition applies to. Possible values are `logs`, `spans`,	`events` and `bizevents`. Changing this attribute will result in deleting and re-creating the bucket definition
        :param pulumi.Input[str] display_name: The name of the bucket definition when visualized within the UI
        :param pulumi.Input[str] name: The name / id of the bucket definition
        """
        pulumi.set(__self__, "retention", retention)
        pulumi.set(__self__, "table", table)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def retention(self) -> pulumi.Input[int]:
        """
        The retention of stored data in days
        """
        return pulumi.get(self, "retention")

    @retention.setter
    def retention(self, value: pulumi.Input[int]):
        pulumi.set(self, "retention", value)

    @property
    @pulumi.getter
    def table(self) -> pulumi.Input[str]:
        """
        The table the bucket definition applies to. Possible values are `logs`, `spans`,	`events` and `bizevents`. Changing this attribute will result in deleting and re-creating the bucket definition
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: pulumi.Input[str]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket definition when visualized within the UI
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name / id of the bucket definition
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PlatformBucketState:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 retention: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PlatformBucket resources.
        :param pulumi.Input[str] display_name: The name of the bucket definition when visualized within the UI
        :param pulumi.Input[str] name: The name / id of the bucket definition
        :param pulumi.Input[int] retention: The retention of stored data in days
        :param pulumi.Input[str] status: The status of the bucket definition. Usually has the value `active` unless an update or delete is currently happening
        :param pulumi.Input[str] table: The table the bucket definition applies to. Possible values are `logs`, `spans`,	`events` and `bizevents`. Changing this attribute will result in deleting and re-creating the bucket definition
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if retention is not None:
            pulumi.set(__self__, "retention", retention)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if table is not None:
            pulumi.set(__self__, "table", table)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket definition when visualized within the UI
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name / id of the bucket definition
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[int]]:
        """
        The retention of stored data in days
        """
        return pulumi.get(self, "retention")

    @retention.setter
    def retention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the bucket definition. Usually has the value `active` unless an update or delete is currently happening
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[str]]:
        """
        The table the bucket definition applies to. Possible values are `logs`, `spans`,	`events` and `bizevents`. Changing this attribute will result in deleting and re-creating the bucket definition
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table", value)


class PlatformBucket(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 retention: Optional[pulumi.Input[int]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a PlatformBucket resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The name of the bucket definition when visualized within the UI
        :param pulumi.Input[str] name: The name / id of the bucket definition
        :param pulumi.Input[int] retention: The retention of stored data in days
        :param pulumi.Input[str] table: The table the bucket definition applies to. Possible values are `logs`, `spans`,	`events` and `bizevents`. Changing this attribute will result in deleting and re-creating the bucket definition
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PlatformBucketArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a PlatformBucket resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PlatformBucketArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PlatformBucketArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 retention: Optional[pulumi.Input[int]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PlatformBucketArgs.__new__(PlatformBucketArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["name"] = name
            if retention is None and not opts.urn:
                raise TypeError("Missing required property 'retention'")
            __props__.__dict__["retention"] = retention
            if table is None and not opts.urn:
                raise TypeError("Missing required property 'table'")
            __props__.__dict__["table"] = table
            __props__.__dict__["status"] = None
        super(PlatformBucket, __self__).__init__(
            'dynatrace:index/platformBucket:PlatformBucket',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            retention: Optional[pulumi.Input[int]] = None,
            status: Optional[pulumi.Input[str]] = None,
            table: Optional[pulumi.Input[str]] = None) -> 'PlatformBucket':
        """
        Get an existing PlatformBucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The name of the bucket definition when visualized within the UI
        :param pulumi.Input[str] name: The name / id of the bucket definition
        :param pulumi.Input[int] retention: The retention of stored data in days
        :param pulumi.Input[str] status: The status of the bucket definition. Usually has the value `active` unless an update or delete is currently happening
        :param pulumi.Input[str] table: The table the bucket definition applies to. Possible values are `logs`, `spans`,	`events` and `bizevents`. Changing this attribute will result in deleting and re-creating the bucket definition
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PlatformBucketState.__new__(_PlatformBucketState)

        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["name"] = name
        __props__.__dict__["retention"] = retention
        __props__.__dict__["status"] = status
        __props__.__dict__["table"] = table
        return PlatformBucket(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the bucket definition when visualized within the UI
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name / id of the bucket definition
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def retention(self) -> pulumi.Output[int]:
        """
        The retention of stored data in days
        """
        return pulumi.get(self, "retention")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the bucket definition. Usually has the value `active` unless an update or delete is currently happening
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def table(self) -> pulumi.Output[str]:
        """
        The table the bucket definition applies to. Possible values are `logs`, `spans`,	`events` and `bizevents`. Changing this attribute will result in deleting and re-creating the bucket definition
        """
        return pulumi.get(self, "table")

