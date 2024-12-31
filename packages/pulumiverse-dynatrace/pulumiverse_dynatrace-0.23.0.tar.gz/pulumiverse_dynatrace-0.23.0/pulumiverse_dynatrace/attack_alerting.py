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

__all__ = ['AttackAlertingArgs', 'AttackAlerting']

@pulumi.input_type
class AttackAlertingArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 enabled_attack_mitigations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AttackAlerting resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_attack_mitigations: Attack State
        :param pulumi.Input[str] name: Name
        """
        pulumi.set(__self__, "enabled", enabled)
        if enabled_attack_mitigations is not None:
            pulumi.set(__self__, "enabled_attack_mitigations", enabled_attack_mitigations)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        This setting is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="enabledAttackMitigations")
    def enabled_attack_mitigations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Attack State
        """
        return pulumi.get(self, "enabled_attack_mitigations")

    @enabled_attack_mitigations.setter
    def enabled_attack_mitigations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_attack_mitigations", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AttackAlertingState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 enabled_attack_mitigations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AttackAlerting resources.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_attack_mitigations: Attack State
        :param pulumi.Input[str] name: Name
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if enabled_attack_mitigations is not None:
            pulumi.set(__self__, "enabled_attack_mitigations", enabled_attack_mitigations)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        This setting is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="enabledAttackMitigations")
    def enabled_attack_mitigations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Attack State
        """
        return pulumi.get(self, "enabled_attack_mitigations")

    @enabled_attack_mitigations.setter
    def enabled_attack_mitigations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_attack_mitigations", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class AttackAlerting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 enabled_attack_mitigations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AttackAlerting resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_attack_mitigations: Attack State
        :param pulumi.Input[str] name: Name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttackAlertingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AttackAlerting resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AttackAlertingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttackAlertingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 enabled_attack_mitigations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttackAlertingArgs.__new__(AttackAlertingArgs)

            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["enabled_attack_mitigations"] = enabled_attack_mitigations
            __props__.__dict__["name"] = name
        super(AttackAlerting, __self__).__init__(
            'dynatrace:index/attackAlerting:AttackAlerting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            enabled_attack_mitigations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'AttackAlerting':
        """
        Get an existing AttackAlerting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_attack_mitigations: Attack State
        :param pulumi.Input[str] name: Name
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AttackAlertingState.__new__(_AttackAlertingState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["enabled_attack_mitigations"] = enabled_attack_mitigations
        __props__.__dict__["name"] = name
        return AttackAlerting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        This setting is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="enabledAttackMitigations")
    def enabled_attack_mitigations(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Attack State
        """
        return pulumi.get(self, "enabled_attack_mitigations")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name
        """
        return pulumi.get(self, "name")

