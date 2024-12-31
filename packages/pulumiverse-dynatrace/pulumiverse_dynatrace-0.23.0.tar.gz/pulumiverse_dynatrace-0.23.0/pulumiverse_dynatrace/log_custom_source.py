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

__all__ = ['LogCustomSourceArgs', 'LogCustomSource']

@pulumi.input_type
class LogCustomSourceArgs:
    def __init__(__self__, *,
                 custom_log_source: pulumi.Input['LogCustomSourceCustomLogSourceArgs'],
                 enabled: pulumi.Input[bool],
                 context: Optional[pulumi.Input['LogCustomSourceContextArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LogCustomSource resource.
        :param pulumi.Input['LogCustomSourceCustomLogSourceArgs'] custom_log_source: no documentation available
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input['LogCustomSourceContextArgs'] context: Define Custom Log Source only within context if provided
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        pulumi.set(__self__, "custom_log_source", custom_log_source)
        pulumi.set(__self__, "enabled", enabled)
        if context is not None:
            pulumi.set(__self__, "context", context)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter(name="customLogSource")
    def custom_log_source(self) -> pulumi.Input['LogCustomSourceCustomLogSourceArgs']:
        """
        no documentation available
        """
        return pulumi.get(self, "custom_log_source")

    @custom_log_source.setter
    def custom_log_source(self, value: pulumi.Input['LogCustomSourceCustomLogSourceArgs']):
        pulumi.set(self, "custom_log_source", value)

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
    def context(self) -> Optional[pulumi.Input['LogCustomSourceContextArgs']]:
        """
        Define Custom Log Source only within context if provided
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input['LogCustomSourceContextArgs']]):
        pulumi.set(self, "context", value)

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

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


@pulumi.input_type
class _LogCustomSourceState:
    def __init__(__self__, *,
                 context: Optional[pulumi.Input['LogCustomSourceContextArgs']] = None,
                 custom_log_source: Optional[pulumi.Input['LogCustomSourceCustomLogSourceArgs']] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LogCustomSource resources.
        :param pulumi.Input['LogCustomSourceContextArgs'] context: Define Custom Log Source only within context if provided
        :param pulumi.Input['LogCustomSourceCustomLogSourceArgs'] custom_log_source: no documentation available
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        if context is not None:
            pulumi.set(__self__, "context", context)
        if custom_log_source is not None:
            pulumi.set(__self__, "custom_log_source", custom_log_source)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input['LogCustomSourceContextArgs']]:
        """
        Define Custom Log Source only within context if provided
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input['LogCustomSourceContextArgs']]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="customLogSource")
    def custom_log_source(self) -> Optional[pulumi.Input['LogCustomSourceCustomLogSourceArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "custom_log_source")

    @custom_log_source.setter
    def custom_log_source(self, value: Optional[pulumi.Input['LogCustomSourceCustomLogSourceArgs']]):
        pulumi.set(self, "custom_log_source", value)

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
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class LogCustomSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[Union['LogCustomSourceContextArgs', 'LogCustomSourceContextArgsDict']]] = None,
                 custom_log_source: Optional[pulumi.Input[Union['LogCustomSourceCustomLogSourceArgs', 'LogCustomSourceCustomLogSourceArgsDict']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a LogCustomSource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['LogCustomSourceContextArgs', 'LogCustomSourceContextArgsDict']] context: Define Custom Log Source only within context if provided
        :param pulumi.Input[Union['LogCustomSourceCustomLogSourceArgs', 'LogCustomSourceCustomLogSourceArgsDict']] custom_log_source: no documentation available
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogCustomSourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a LogCustomSource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param LogCustomSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogCustomSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[Union['LogCustomSourceContextArgs', 'LogCustomSourceContextArgsDict']]] = None,
                 custom_log_source: Optional[pulumi.Input[Union['LogCustomSourceCustomLogSourceArgs', 'LogCustomSourceCustomLogSourceArgsDict']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogCustomSourceArgs.__new__(LogCustomSourceArgs)

            __props__.__dict__["context"] = context
            if custom_log_source is None and not opts.urn:
                raise TypeError("Missing required property 'custom_log_source'")
            __props__.__dict__["custom_log_source"] = custom_log_source
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["scope"] = scope
        super(LogCustomSource, __self__).__init__(
            'dynatrace:index/logCustomSource:LogCustomSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            context: Optional[pulumi.Input[Union['LogCustomSourceContextArgs', 'LogCustomSourceContextArgsDict']]] = None,
            custom_log_source: Optional[pulumi.Input[Union['LogCustomSourceCustomLogSourceArgs', 'LogCustomSourceCustomLogSourceArgsDict']]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'LogCustomSource':
        """
        Get an existing LogCustomSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['LogCustomSourceContextArgs', 'LogCustomSourceContextArgsDict']] context: Define Custom Log Source only within context if provided
        :param pulumi.Input[Union['LogCustomSourceCustomLogSourceArgs', 'LogCustomSourceCustomLogSourceArgsDict']] custom_log_source: no documentation available
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogCustomSourceState.__new__(_LogCustomSourceState)

        __props__.__dict__["context"] = context
        __props__.__dict__["custom_log_source"] = custom_log_source
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["scope"] = scope
        return LogCustomSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional['outputs.LogCustomSourceContext']]:
        """
        Define Custom Log Source only within context if provided
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="customLogSource")
    def custom_log_source(self) -> pulumi.Output['outputs.LogCustomSourceCustomLogSource']:
        """
        no documentation available
        """
        return pulumi.get(self, "custom_log_source")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        This setting is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        return pulumi.get(self, "scope")

