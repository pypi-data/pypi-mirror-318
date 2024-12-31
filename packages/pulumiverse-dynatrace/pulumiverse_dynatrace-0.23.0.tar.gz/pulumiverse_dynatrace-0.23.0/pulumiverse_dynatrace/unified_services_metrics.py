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

__all__ = ['UnifiedServicesMetricsArgs', 'UnifiedServicesMetrics']

@pulumi.input_type
class UnifiedServicesMetricsArgs:
    def __init__(__self__, *,
                 enable_endpoint_metrics: pulumi.Input[bool],
                 service_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UnifiedServicesMetrics resource.
        :param pulumi.Input[bool] enable_endpoint_metrics: Should metrics be written for endpoints? Please be aware that this setting has billing implications. Check out this [documentation](https://dt-url.net/td23cgh) for further details.
        :param pulumi.Input[str] service_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        pulumi.set(__self__, "enable_endpoint_metrics", enable_endpoint_metrics)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)

    @property
    @pulumi.getter(name="enableEndpointMetrics")
    def enable_endpoint_metrics(self) -> pulumi.Input[bool]:
        """
        Should metrics be written for endpoints? Please be aware that this setting has billing implications. Check out this [documentation](https://dt-url.net/td23cgh) for further details.
        """
        return pulumi.get(self, "enable_endpoint_metrics")

    @enable_endpoint_metrics.setter
    def enable_endpoint_metrics(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_endpoint_metrics", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_id", value)


@pulumi.input_type
class _UnifiedServicesMetricsState:
    def __init__(__self__, *,
                 enable_endpoint_metrics: Optional[pulumi.Input[bool]] = None,
                 service_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UnifiedServicesMetrics resources.
        :param pulumi.Input[bool] enable_endpoint_metrics: Should metrics be written for endpoints? Please be aware that this setting has billing implications. Check out this [documentation](https://dt-url.net/td23cgh) for further details.
        :param pulumi.Input[str] service_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        if enable_endpoint_metrics is not None:
            pulumi.set(__self__, "enable_endpoint_metrics", enable_endpoint_metrics)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)

    @property
    @pulumi.getter(name="enableEndpointMetrics")
    def enable_endpoint_metrics(self) -> Optional[pulumi.Input[bool]]:
        """
        Should metrics be written for endpoints? Please be aware that this setting has billing implications. Check out this [documentation](https://dt-url.net/td23cgh) for further details.
        """
        return pulumi.get(self, "enable_endpoint_metrics")

    @enable_endpoint_metrics.setter
    def enable_endpoint_metrics(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_endpoint_metrics", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_id", value)


class UnifiedServicesMetrics(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_endpoint_metrics: Optional[pulumi.Input[bool]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a UnifiedServicesMetrics resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_endpoint_metrics: Should metrics be written for endpoints? Please be aware that this setting has billing implications. Check out this [documentation](https://dt-url.net/td23cgh) for further details.
        :param pulumi.Input[str] service_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UnifiedServicesMetricsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a UnifiedServicesMetrics resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param UnifiedServicesMetricsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UnifiedServicesMetricsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_endpoint_metrics: Optional[pulumi.Input[bool]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UnifiedServicesMetricsArgs.__new__(UnifiedServicesMetricsArgs)

            if enable_endpoint_metrics is None and not opts.urn:
                raise TypeError("Missing required property 'enable_endpoint_metrics'")
            __props__.__dict__["enable_endpoint_metrics"] = enable_endpoint_metrics
            __props__.__dict__["service_id"] = service_id
        super(UnifiedServicesMetrics, __self__).__init__(
            'dynatrace:index/unifiedServicesMetrics:UnifiedServicesMetrics',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable_endpoint_metrics: Optional[pulumi.Input[bool]] = None,
            service_id: Optional[pulumi.Input[str]] = None) -> 'UnifiedServicesMetrics':
        """
        Get an existing UnifiedServicesMetrics resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_endpoint_metrics: Should metrics be written for endpoints? Please be aware that this setting has billing implications. Check out this [documentation](https://dt-url.net/td23cgh) for further details.
        :param pulumi.Input[str] service_id: The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UnifiedServicesMetricsState.__new__(_UnifiedServicesMetricsState)

        __props__.__dict__["enable_endpoint_metrics"] = enable_endpoint_metrics
        __props__.__dict__["service_id"] = service_id
        return UnifiedServicesMetrics(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="enableEndpointMetrics")
    def enable_endpoint_metrics(self) -> pulumi.Output[bool]:
        """
        Should metrics be written for endpoints? Please be aware that this setting has billing implications. Check out this [documentation](https://dt-url.net/td23cgh) for further details.
        """
        return pulumi.get(self, "enable_endpoint_metrics")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[Optional[str]]:
        """
        The scope of this settings. If the settings should cover the whole environment, just don't specify any scope.
        """
        return pulumi.get(self, "service_id")

