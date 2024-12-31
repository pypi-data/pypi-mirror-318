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

__all__ = ['OneagentFeaturesArgs', 'OneagentFeatures']

@pulumi.input_type
class OneagentFeaturesArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 key: pulumi.Input[str],
                 forcible: Optional[pulumi.Input[bool]] = None,
                 instrumentation: Optional[pulumi.Input[bool]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OneagentFeatures resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] key: Feature
        :param pulumi.Input[bool] forcible: Activate this feature also in OneAgents only fulfilling the minimum Opt-In version
        :param pulumi.Input[bool] instrumentation: Instrumentation enabled (change needs a process restart)
        :param pulumi.Input[str] scope: The scope of this setting (PROCESS*GROUP*INSTANCE, PROCESS_GROUP). Omit this property if you want to cover the whole environment.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "key", key)
        if forcible is not None:
            pulumi.set(__self__, "forcible", forcible)
        if instrumentation is not None:
            pulumi.set(__self__, "instrumentation", instrumentation)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

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
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Feature
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def forcible(self) -> Optional[pulumi.Input[bool]]:
        """
        Activate this feature also in OneAgents only fulfilling the minimum Opt-In version
        """
        return pulumi.get(self, "forcible")

    @forcible.setter
    def forcible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "forcible", value)

    @property
    @pulumi.getter
    def instrumentation(self) -> Optional[pulumi.Input[bool]]:
        """
        Instrumentation enabled (change needs a process restart)
        """
        return pulumi.get(self, "instrumentation")

    @instrumentation.setter
    def instrumentation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "instrumentation", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this setting (PROCESS*GROUP*INSTANCE, PROCESS_GROUP). Omit this property if you want to cover the whole environment.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


@pulumi.input_type
class _OneagentFeaturesState:
    def __init__(__self__, *,
                 _restore_: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 forcible: Optional[pulumi.Input[bool]] = None,
                 instrumentation: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OneagentFeatures resources.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] forcible: Activate this feature also in OneAgents only fulfilling the minimum Opt-In version
        :param pulumi.Input[bool] instrumentation: Instrumentation enabled (change needs a process restart)
        :param pulumi.Input[str] key: Feature
        :param pulumi.Input[str] scope: The scope of this setting (PROCESS*GROUP*INSTANCE, PROCESS_GROUP). Omit this property if you want to cover the whole environment.
        """
        if _restore_ is not None:
            pulumi.set(__self__, "_restore_", _restore_)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if forcible is not None:
            pulumi.set(__self__, "forcible", forcible)
        if instrumentation is not None:
            pulumi.set(__self__, "instrumentation", instrumentation)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def _restore_(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "_restore_")

    @_restore_.setter
    def _restore_(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "_restore_", value)

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
    @pulumi.getter
    def forcible(self) -> Optional[pulumi.Input[bool]]:
        """
        Activate this feature also in OneAgents only fulfilling the minimum Opt-In version
        """
        return pulumi.get(self, "forcible")

    @forcible.setter
    def forcible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "forcible", value)

    @property
    @pulumi.getter
    def instrumentation(self) -> Optional[pulumi.Input[bool]]:
        """
        Instrumentation enabled (change needs a process restart)
        """
        return pulumi.get(self, "instrumentation")

    @instrumentation.setter
    def instrumentation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "instrumentation", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Feature
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this setting (PROCESS*GROUP*INSTANCE, PROCESS_GROUP). Omit this property if you want to cover the whole environment.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class OneagentFeatures(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 forcible: Optional[pulumi.Input[bool]] = None,
                 instrumentation: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a OneagentFeatures resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] forcible: Activate this feature also in OneAgents only fulfilling the minimum Opt-In version
        :param pulumi.Input[bool] instrumentation: Instrumentation enabled (change needs a process restart)
        :param pulumi.Input[str] key: Feature
        :param pulumi.Input[str] scope: The scope of this setting (PROCESS*GROUP*INSTANCE, PROCESS_GROUP). Omit this property if you want to cover the whole environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OneagentFeaturesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OneagentFeatures resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OneagentFeaturesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OneagentFeaturesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 forcible: Optional[pulumi.Input[bool]] = None,
                 instrumentation: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OneagentFeaturesArgs.__new__(OneagentFeaturesArgs)

            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["forcible"] = forcible
            __props__.__dict__["instrumentation"] = instrumentation
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["scope"] = scope
            __props__.__dict__["_restore_"] = None
        super(OneagentFeatures, __self__).__init__(
            'dynatrace:index/oneagentFeatures:OneagentFeatures',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            _restore_: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            forcible: Optional[pulumi.Input[bool]] = None,
            instrumentation: Optional[pulumi.Input[bool]] = None,
            key: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'OneagentFeatures':
        """
        Get an existing OneagentFeatures resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] forcible: Activate this feature also in OneAgents only fulfilling the minimum Opt-In version
        :param pulumi.Input[bool] instrumentation: Instrumentation enabled (change needs a process restart)
        :param pulumi.Input[str] key: Feature
        :param pulumi.Input[str] scope: The scope of this setting (PROCESS*GROUP*INSTANCE, PROCESS_GROUP). Omit this property if you want to cover the whole environment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OneagentFeaturesState.__new__(_OneagentFeaturesState)

        __props__.__dict__["_restore_"] = _restore_
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["forcible"] = forcible
        __props__.__dict__["instrumentation"] = instrumentation
        __props__.__dict__["key"] = key
        __props__.__dict__["scope"] = scope
        return OneagentFeatures(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def _restore_(self) -> pulumi.Output[str]:
        return pulumi.get(self, "_restore_")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        This setting is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def forcible(self) -> pulumi.Output[Optional[bool]]:
        """
        Activate this feature also in OneAgents only fulfilling the minimum Opt-In version
        """
        return pulumi.get(self, "forcible")

    @property
    @pulumi.getter
    def instrumentation(self) -> pulumi.Output[Optional[bool]]:
        """
        Instrumentation enabled (change needs a process restart)
        """
        return pulumi.get(self, "instrumentation")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        Feature
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope of this setting (PROCESS*GROUP*INSTANCE, PROCESS_GROUP). Omit this property if you want to cover the whole environment.
        """
        return pulumi.get(self, "scope")

