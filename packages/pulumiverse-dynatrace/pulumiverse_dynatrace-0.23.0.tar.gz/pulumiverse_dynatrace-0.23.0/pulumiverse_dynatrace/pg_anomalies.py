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

__all__ = ['PgAnomaliesArgs', 'PgAnomalies']

@pulumi.input_type
class PgAnomaliesArgs:
    def __init__(__self__, *,
                 pg_id: pulumi.Input[str],
                 availability: Optional[pulumi.Input['PgAnomaliesAvailabilityArgs']] = None):
        """
        The set of arguments for constructing a PgAnomalies resource.
        :param pulumi.Input[str] pg_id: The ID of the process group
        :param pulumi.Input['PgAnomaliesAvailabilityArgs'] availability: Configuration of the availability monitoring for the process group.
        """
        pulumi.set(__self__, "pg_id", pg_id)
        if availability is not None:
            pulumi.set(__self__, "availability", availability)

    @property
    @pulumi.getter(name="pgId")
    def pg_id(self) -> pulumi.Input[str]:
        """
        The ID of the process group
        """
        return pulumi.get(self, "pg_id")

    @pg_id.setter
    def pg_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "pg_id", value)

    @property
    @pulumi.getter
    def availability(self) -> Optional[pulumi.Input['PgAnomaliesAvailabilityArgs']]:
        """
        Configuration of the availability monitoring for the process group.
        """
        return pulumi.get(self, "availability")

    @availability.setter
    def availability(self, value: Optional[pulumi.Input['PgAnomaliesAvailabilityArgs']]):
        pulumi.set(self, "availability", value)


@pulumi.input_type
class _PgAnomaliesState:
    def __init__(__self__, *,
                 availability: Optional[pulumi.Input['PgAnomaliesAvailabilityArgs']] = None,
                 pg_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PgAnomalies resources.
        :param pulumi.Input['PgAnomaliesAvailabilityArgs'] availability: Configuration of the availability monitoring for the process group.
        :param pulumi.Input[str] pg_id: The ID of the process group
        """
        if availability is not None:
            pulumi.set(__self__, "availability", availability)
        if pg_id is not None:
            pulumi.set(__self__, "pg_id", pg_id)

    @property
    @pulumi.getter
    def availability(self) -> Optional[pulumi.Input['PgAnomaliesAvailabilityArgs']]:
        """
        Configuration of the availability monitoring for the process group.
        """
        return pulumi.get(self, "availability")

    @availability.setter
    def availability(self, value: Optional[pulumi.Input['PgAnomaliesAvailabilityArgs']]):
        pulumi.set(self, "availability", value)

    @property
    @pulumi.getter(name="pgId")
    def pg_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the process group
        """
        return pulumi.get(self, "pg_id")

    @pg_id.setter
    def pg_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pg_id", value)


class PgAnomalies(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability: Optional[pulumi.Input[Union['PgAnomaliesAvailabilityArgs', 'PgAnomaliesAvailabilityArgsDict']]] = None,
                 pg_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a PgAnomalies resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['PgAnomaliesAvailabilityArgs', 'PgAnomaliesAvailabilityArgsDict']] availability: Configuration of the availability monitoring for the process group.
        :param pulumi.Input[str] pg_id: The ID of the process group
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PgAnomaliesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a PgAnomalies resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PgAnomaliesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PgAnomaliesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability: Optional[pulumi.Input[Union['PgAnomaliesAvailabilityArgs', 'PgAnomaliesAvailabilityArgsDict']]] = None,
                 pg_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PgAnomaliesArgs.__new__(PgAnomaliesArgs)

            __props__.__dict__["availability"] = availability
            if pg_id is None and not opts.urn:
                raise TypeError("Missing required property 'pg_id'")
            __props__.__dict__["pg_id"] = pg_id
        super(PgAnomalies, __self__).__init__(
            'dynatrace:index/pgAnomalies:PgAnomalies',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            availability: Optional[pulumi.Input[Union['PgAnomaliesAvailabilityArgs', 'PgAnomaliesAvailabilityArgsDict']]] = None,
            pg_id: Optional[pulumi.Input[str]] = None) -> 'PgAnomalies':
        """
        Get an existing PgAnomalies resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['PgAnomaliesAvailabilityArgs', 'PgAnomaliesAvailabilityArgsDict']] availability: Configuration of the availability monitoring for the process group.
        :param pulumi.Input[str] pg_id: The ID of the process group
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PgAnomaliesState.__new__(_PgAnomaliesState)

        __props__.__dict__["availability"] = availability
        __props__.__dict__["pg_id"] = pg_id
        return PgAnomalies(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def availability(self) -> pulumi.Output[Optional['outputs.PgAnomaliesAvailability']]:
        """
        Configuration of the availability monitoring for the process group.
        """
        return pulumi.get(self, "availability")

    @property
    @pulumi.getter(name="pgId")
    def pg_id(self) -> pulumi.Output[str]:
        """
        The ID of the process group
        """
        return pulumi.get(self, "pg_id")

