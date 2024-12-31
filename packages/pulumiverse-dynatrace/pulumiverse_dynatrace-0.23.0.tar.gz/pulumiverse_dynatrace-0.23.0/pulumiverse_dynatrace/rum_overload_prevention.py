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

__all__ = ['RumOverloadPreventionArgs', 'RumOverloadPrevention']

@pulumi.input_type
class RumOverloadPreventionArgs:
    def __init__(__self__, *,
                 overload_prevention_limit: pulumi.Input[int]):
        """
        The set of arguments for constructing a RumOverloadPrevention resource.
        :param pulumi.Input[int] overload_prevention_limit: Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).
        """
        pulumi.set(__self__, "overload_prevention_limit", overload_prevention_limit)

    @property
    @pulumi.getter(name="overloadPreventionLimit")
    def overload_prevention_limit(self) -> pulumi.Input[int]:
        """
        Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).
        """
        return pulumi.get(self, "overload_prevention_limit")

    @overload_prevention_limit.setter
    def overload_prevention_limit(self, value: pulumi.Input[int]):
        pulumi.set(self, "overload_prevention_limit", value)


@pulumi.input_type
class _RumOverloadPreventionState:
    def __init__(__self__, *,
                 overload_prevention_limit: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering RumOverloadPrevention resources.
        :param pulumi.Input[int] overload_prevention_limit: Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).
        """
        if overload_prevention_limit is not None:
            pulumi.set(__self__, "overload_prevention_limit", overload_prevention_limit)

    @property
    @pulumi.getter(name="overloadPreventionLimit")
    def overload_prevention_limit(self) -> Optional[pulumi.Input[int]]:
        """
        Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).
        """
        return pulumi.get(self, "overload_prevention_limit")

    @overload_prevention_limit.setter
    def overload_prevention_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "overload_prevention_limit", value)


class RumOverloadPrevention(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 overload_prevention_limit: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a RumOverloadPrevention resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] overload_prevention_limit: Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RumOverloadPreventionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a RumOverloadPrevention resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param RumOverloadPreventionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RumOverloadPreventionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 overload_prevention_limit: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RumOverloadPreventionArgs.__new__(RumOverloadPreventionArgs)

            if overload_prevention_limit is None and not opts.urn:
                raise TypeError("Missing required property 'overload_prevention_limit'")
            __props__.__dict__["overload_prevention_limit"] = overload_prevention_limit
        super(RumOverloadPrevention, __self__).__init__(
            'dynatrace:index/rumOverloadPrevention:RumOverloadPrevention',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            overload_prevention_limit: Optional[pulumi.Input[int]] = None) -> 'RumOverloadPrevention':
        """
        Get an existing RumOverloadPrevention resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] overload_prevention_limit: Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RumOverloadPreventionState.__new__(_RumOverloadPreventionState)

        __props__.__dict__["overload_prevention_limit"] = overload_prevention_limit
        return RumOverloadPrevention(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="overloadPreventionLimit")
    def overload_prevention_limit(self) -> pulumi.Output[int]:
        """
        Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).
        """
        return pulumi.get(self, "overload_prevention_limit")

