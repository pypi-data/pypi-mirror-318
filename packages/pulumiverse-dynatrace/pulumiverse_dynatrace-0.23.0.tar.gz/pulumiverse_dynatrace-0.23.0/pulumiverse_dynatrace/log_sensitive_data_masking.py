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

__all__ = ['LogSensitiveDataMaskingArgs', 'LogSensitiveDataMasking']

@pulumi.input_type
class LogSensitiveDataMaskingArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 masking: pulumi.Input['LogSensitiveDataMaskingMaskingArgs'],
                 insert_after: Optional[pulumi.Input[str]] = None,
                 matchers: Optional[pulumi.Input['LogSensitiveDataMaskingMatchersArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LogSensitiveDataMasking resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input['LogSensitiveDataMaskingMaskingArgs'] masking: no documentation available
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input['LogSensitiveDataMaskingMatchersArgs'] matchers: no documentation available
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "masking", masking)
        if insert_after is not None:
            pulumi.set(__self__, "insert_after", insert_after)
        if matchers is not None:
            pulumi.set(__self__, "matchers", matchers)
        if name is not None:
            pulumi.set(__self__, "name", name)
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
    def masking(self) -> pulumi.Input['LogSensitiveDataMaskingMaskingArgs']:
        """
        no documentation available
        """
        return pulumi.get(self, "masking")

    @masking.setter
    def masking(self, value: pulumi.Input['LogSensitiveDataMaskingMaskingArgs']):
        pulumi.set(self, "masking", value)

    @property
    @pulumi.getter(name="insertAfter")
    def insert_after(self) -> Optional[pulumi.Input[str]]:
        """
        Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        """
        return pulumi.get(self, "insert_after")

    @insert_after.setter
    def insert_after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "insert_after", value)

    @property
    @pulumi.getter
    def matchers(self) -> Optional[pulumi.Input['LogSensitiveDataMaskingMatchersArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "matchers")

    @matchers.setter
    def matchers(self, value: Optional[pulumi.Input['LogSensitiveDataMaskingMatchersArgs']]):
        pulumi.set(self, "matchers", value)

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
class _LogSensitiveDataMaskingState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 masking: Optional[pulumi.Input['LogSensitiveDataMaskingMaskingArgs']] = None,
                 matchers: Optional[pulumi.Input['LogSensitiveDataMaskingMatchersArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LogSensitiveDataMasking resources.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input['LogSensitiveDataMaskingMaskingArgs'] masking: no documentation available
        :param pulumi.Input['LogSensitiveDataMaskingMatchersArgs'] matchers: no documentation available
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if insert_after is not None:
            pulumi.set(__self__, "insert_after", insert_after)
        if masking is not None:
            pulumi.set(__self__, "masking", masking)
        if matchers is not None:
            pulumi.set(__self__, "matchers", matchers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

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
    @pulumi.getter(name="insertAfter")
    def insert_after(self) -> Optional[pulumi.Input[str]]:
        """
        Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        """
        return pulumi.get(self, "insert_after")

    @insert_after.setter
    def insert_after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "insert_after", value)

    @property
    @pulumi.getter
    def masking(self) -> Optional[pulumi.Input['LogSensitiveDataMaskingMaskingArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "masking")

    @masking.setter
    def masking(self, value: Optional[pulumi.Input['LogSensitiveDataMaskingMaskingArgs']]):
        pulumi.set(self, "masking", value)

    @property
    @pulumi.getter
    def matchers(self) -> Optional[pulumi.Input['LogSensitiveDataMaskingMatchersArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "matchers")

    @matchers.setter
    def matchers(self, value: Optional[pulumi.Input['LogSensitiveDataMaskingMatchersArgs']]):
        pulumi.set(self, "matchers", value)

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


class LogSensitiveDataMasking(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 masking: Optional[pulumi.Input[Union['LogSensitiveDataMaskingMaskingArgs', 'LogSensitiveDataMaskingMaskingArgsDict']]] = None,
                 matchers: Optional[pulumi.Input[Union['LogSensitiveDataMaskingMatchersArgs', 'LogSensitiveDataMaskingMatchersArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a LogSensitiveDataMasking resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[Union['LogSensitiveDataMaskingMaskingArgs', 'LogSensitiveDataMaskingMaskingArgsDict']] masking: no documentation available
        :param pulumi.Input[Union['LogSensitiveDataMaskingMatchersArgs', 'LogSensitiveDataMaskingMatchersArgsDict']] matchers: no documentation available
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogSensitiveDataMaskingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a LogSensitiveDataMasking resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param LogSensitiveDataMaskingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogSensitiveDataMaskingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 masking: Optional[pulumi.Input[Union['LogSensitiveDataMaskingMaskingArgs', 'LogSensitiveDataMaskingMaskingArgsDict']]] = None,
                 matchers: Optional[pulumi.Input[Union['LogSensitiveDataMaskingMatchersArgs', 'LogSensitiveDataMaskingMatchersArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogSensitiveDataMaskingArgs.__new__(LogSensitiveDataMaskingArgs)

            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["insert_after"] = insert_after
            if masking is None and not opts.urn:
                raise TypeError("Missing required property 'masking'")
            __props__.__dict__["masking"] = masking
            __props__.__dict__["matchers"] = matchers
            __props__.__dict__["name"] = name
            __props__.__dict__["scope"] = scope
        super(LogSensitiveDataMasking, __self__).__init__(
            'dynatrace:index/logSensitiveDataMasking:LogSensitiveDataMasking',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            insert_after: Optional[pulumi.Input[str]] = None,
            masking: Optional[pulumi.Input[Union['LogSensitiveDataMaskingMaskingArgs', 'LogSensitiveDataMaskingMaskingArgsDict']]] = None,
            matchers: Optional[pulumi.Input[Union['LogSensitiveDataMaskingMatchersArgs', 'LogSensitiveDataMaskingMatchersArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'LogSensitiveDataMasking':
        """
        Get an existing LogSensitiveDataMasking resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[Union['LogSensitiveDataMaskingMaskingArgs', 'LogSensitiveDataMaskingMaskingArgsDict']] masking: no documentation available
        :param pulumi.Input[Union['LogSensitiveDataMaskingMatchersArgs', 'LogSensitiveDataMaskingMatchersArgsDict']] matchers: no documentation available
        :param pulumi.Input[str] name: Name
        :param pulumi.Input[str] scope: The scope of this setting (HOST, KUBERNETES*CLUSTER, HOST*GROUP). Omit this property if you want to cover the whole environment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogSensitiveDataMaskingState.__new__(_LogSensitiveDataMaskingState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["insert_after"] = insert_after
        __props__.__dict__["masking"] = masking
        __props__.__dict__["matchers"] = matchers
        __props__.__dict__["name"] = name
        __props__.__dict__["scope"] = scope
        return LogSensitiveDataMasking(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        This setting is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="insertAfter")
    def insert_after(self) -> pulumi.Output[str]:
        """
        Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        """
        return pulumi.get(self, "insert_after")

    @property
    @pulumi.getter
    def masking(self) -> pulumi.Output['outputs.LogSensitiveDataMaskingMasking']:
        """
        no documentation available
        """
        return pulumi.get(self, "masking")

    @property
    @pulumi.getter
    def matchers(self) -> pulumi.Output[Optional['outputs.LogSensitiveDataMaskingMatchers']]:
        """
        no documentation available
        """
        return pulumi.get(self, "matchers")

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

