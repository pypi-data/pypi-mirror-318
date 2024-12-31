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

__all__ = ['InfraopsAppSettingsArgs', 'InfraopsAppSettings']

@pulumi.input_type
class InfraopsAppSettingsArgs:
    def __init__(__self__, *,
                 show_monitoring_candidates: pulumi.Input[bool],
                 show_standalone_hosts: pulumi.Input[bool],
                 interface_saturation_threshold: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a InfraopsAppSettings resource.
        :param pulumi.Input[bool] show_monitoring_candidates: When set to true, the app will display monitoring candidates in the Hosts table
        :param pulumi.Input[bool] show_standalone_hosts: When set to true, the app will display app only hosts in the Hosts table
        :param pulumi.Input[float] interface_saturation_threshold: (Required v305+) The threshold at which a network device interface is deemed to be saturated.
        """
        pulumi.set(__self__, "show_monitoring_candidates", show_monitoring_candidates)
        pulumi.set(__self__, "show_standalone_hosts", show_standalone_hosts)
        if interface_saturation_threshold is not None:
            pulumi.set(__self__, "interface_saturation_threshold", interface_saturation_threshold)

    @property
    @pulumi.getter(name="showMonitoringCandidates")
    def show_monitoring_candidates(self) -> pulumi.Input[bool]:
        """
        When set to true, the app will display monitoring candidates in the Hosts table
        """
        return pulumi.get(self, "show_monitoring_candidates")

    @show_monitoring_candidates.setter
    def show_monitoring_candidates(self, value: pulumi.Input[bool]):
        pulumi.set(self, "show_monitoring_candidates", value)

    @property
    @pulumi.getter(name="showStandaloneHosts")
    def show_standalone_hosts(self) -> pulumi.Input[bool]:
        """
        When set to true, the app will display app only hosts in the Hosts table
        """
        return pulumi.get(self, "show_standalone_hosts")

    @show_standalone_hosts.setter
    def show_standalone_hosts(self, value: pulumi.Input[bool]):
        pulumi.set(self, "show_standalone_hosts", value)

    @property
    @pulumi.getter(name="interfaceSaturationThreshold")
    def interface_saturation_threshold(self) -> Optional[pulumi.Input[float]]:
        """
        (Required v305+) The threshold at which a network device interface is deemed to be saturated.
        """
        return pulumi.get(self, "interface_saturation_threshold")

    @interface_saturation_threshold.setter
    def interface_saturation_threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "interface_saturation_threshold", value)


@pulumi.input_type
class _InfraopsAppSettingsState:
    def __init__(__self__, *,
                 interface_saturation_threshold: Optional[pulumi.Input[float]] = None,
                 show_monitoring_candidates: Optional[pulumi.Input[bool]] = None,
                 show_standalone_hosts: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering InfraopsAppSettings resources.
        :param pulumi.Input[float] interface_saturation_threshold: (Required v305+) The threshold at which a network device interface is deemed to be saturated.
        :param pulumi.Input[bool] show_monitoring_candidates: When set to true, the app will display monitoring candidates in the Hosts table
        :param pulumi.Input[bool] show_standalone_hosts: When set to true, the app will display app only hosts in the Hosts table
        """
        if interface_saturation_threshold is not None:
            pulumi.set(__self__, "interface_saturation_threshold", interface_saturation_threshold)
        if show_monitoring_candidates is not None:
            pulumi.set(__self__, "show_monitoring_candidates", show_monitoring_candidates)
        if show_standalone_hosts is not None:
            pulumi.set(__self__, "show_standalone_hosts", show_standalone_hosts)

    @property
    @pulumi.getter(name="interfaceSaturationThreshold")
    def interface_saturation_threshold(self) -> Optional[pulumi.Input[float]]:
        """
        (Required v305+) The threshold at which a network device interface is deemed to be saturated.
        """
        return pulumi.get(self, "interface_saturation_threshold")

    @interface_saturation_threshold.setter
    def interface_saturation_threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "interface_saturation_threshold", value)

    @property
    @pulumi.getter(name="showMonitoringCandidates")
    def show_monitoring_candidates(self) -> Optional[pulumi.Input[bool]]:
        """
        When set to true, the app will display monitoring candidates in the Hosts table
        """
        return pulumi.get(self, "show_monitoring_candidates")

    @show_monitoring_candidates.setter
    def show_monitoring_candidates(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "show_monitoring_candidates", value)

    @property
    @pulumi.getter(name="showStandaloneHosts")
    def show_standalone_hosts(self) -> Optional[pulumi.Input[bool]]:
        """
        When set to true, the app will display app only hosts in the Hosts table
        """
        return pulumi.get(self, "show_standalone_hosts")

    @show_standalone_hosts.setter
    def show_standalone_hosts(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "show_standalone_hosts", value)


class InfraopsAppSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 interface_saturation_threshold: Optional[pulumi.Input[float]] = None,
                 show_monitoring_candidates: Optional[pulumi.Input[bool]] = None,
                 show_standalone_hosts: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a InfraopsAppSettings resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] interface_saturation_threshold: (Required v305+) The threshold at which a network device interface is deemed to be saturated.
        :param pulumi.Input[bool] show_monitoring_candidates: When set to true, the app will display monitoring candidates in the Hosts table
        :param pulumi.Input[bool] show_standalone_hosts: When set to true, the app will display app only hosts in the Hosts table
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InfraopsAppSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a InfraopsAppSettings resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InfraopsAppSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InfraopsAppSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 interface_saturation_threshold: Optional[pulumi.Input[float]] = None,
                 show_monitoring_candidates: Optional[pulumi.Input[bool]] = None,
                 show_standalone_hosts: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InfraopsAppSettingsArgs.__new__(InfraopsAppSettingsArgs)

            __props__.__dict__["interface_saturation_threshold"] = interface_saturation_threshold
            if show_monitoring_candidates is None and not opts.urn:
                raise TypeError("Missing required property 'show_monitoring_candidates'")
            __props__.__dict__["show_monitoring_candidates"] = show_monitoring_candidates
            if show_standalone_hosts is None and not opts.urn:
                raise TypeError("Missing required property 'show_standalone_hosts'")
            __props__.__dict__["show_standalone_hosts"] = show_standalone_hosts
        super(InfraopsAppSettings, __self__).__init__(
            'dynatrace:index/infraopsAppSettings:InfraopsAppSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            interface_saturation_threshold: Optional[pulumi.Input[float]] = None,
            show_monitoring_candidates: Optional[pulumi.Input[bool]] = None,
            show_standalone_hosts: Optional[pulumi.Input[bool]] = None) -> 'InfraopsAppSettings':
        """
        Get an existing InfraopsAppSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] interface_saturation_threshold: (Required v305+) The threshold at which a network device interface is deemed to be saturated.
        :param pulumi.Input[bool] show_monitoring_candidates: When set to true, the app will display monitoring candidates in the Hosts table
        :param pulumi.Input[bool] show_standalone_hosts: When set to true, the app will display app only hosts in the Hosts table
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InfraopsAppSettingsState.__new__(_InfraopsAppSettingsState)

        __props__.__dict__["interface_saturation_threshold"] = interface_saturation_threshold
        __props__.__dict__["show_monitoring_candidates"] = show_monitoring_candidates
        __props__.__dict__["show_standalone_hosts"] = show_standalone_hosts
        return InfraopsAppSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="interfaceSaturationThreshold")
    def interface_saturation_threshold(self) -> pulumi.Output[Optional[float]]:
        """
        (Required v305+) The threshold at which a network device interface is deemed to be saturated.
        """
        return pulumi.get(self, "interface_saturation_threshold")

    @property
    @pulumi.getter(name="showMonitoringCandidates")
    def show_monitoring_candidates(self) -> pulumi.Output[bool]:
        """
        When set to true, the app will display monitoring candidates in the Hosts table
        """
        return pulumi.get(self, "show_monitoring_candidates")

    @property
    @pulumi.getter(name="showStandaloneHosts")
    def show_standalone_hosts(self) -> pulumi.Output[bool]:
        """
        When set to true, the app will display app only hosts in the Hosts table
        """
        return pulumi.get(self, "show_standalone_hosts")

