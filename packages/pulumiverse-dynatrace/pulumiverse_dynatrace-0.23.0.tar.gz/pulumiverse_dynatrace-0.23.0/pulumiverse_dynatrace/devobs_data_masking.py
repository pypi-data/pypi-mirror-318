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

__all__ = ['DevobsDataMaskingArgs', 'DevobsDataMasking']

@pulumi.input_type
class DevobsDataMaskingArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 replacement_type: pulumi.Input[str],
                 rule_name: pulumi.Input[str],
                 rule_type: pulumi.Input[str],
                 insert_after: Optional[pulumi.Input[str]] = None,
                 replacement_pattern: Optional[pulumi.Input[str]] = None,
                 rule_regex: Optional[pulumi.Input[str]] = None,
                 rule_var_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DevobsDataMasking resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] replacement_type: Possible Values: `SHA256`, `STRING`
        :param pulumi.Input[str] rule_name: Rule Name
        :param pulumi.Input[str] rule_type: Possible Values: `REGEX`, `VAR_NAME`
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] replacement_pattern: no documentation available
        :param pulumi.Input[str] rule_regex: no documentation available
        :param pulumi.Input[str] rule_var_name: no documentation available
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "replacement_type", replacement_type)
        pulumi.set(__self__, "rule_name", rule_name)
        pulumi.set(__self__, "rule_type", rule_type)
        if insert_after is not None:
            pulumi.set(__self__, "insert_after", insert_after)
        if replacement_pattern is not None:
            pulumi.set(__self__, "replacement_pattern", replacement_pattern)
        if rule_regex is not None:
            pulumi.set(__self__, "rule_regex", rule_regex)
        if rule_var_name is not None:
            pulumi.set(__self__, "rule_var_name", rule_var_name)

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
    @pulumi.getter(name="replacementType")
    def replacement_type(self) -> pulumi.Input[str]:
        """
        Possible Values: `SHA256`, `STRING`
        """
        return pulumi.get(self, "replacement_type")

    @replacement_type.setter
    def replacement_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "replacement_type", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[str]:
        """
        Rule Name
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[str]:
        """
        Possible Values: `REGEX`, `VAR_NAME`
        """
        return pulumi.get(self, "rule_type")

    @rule_type.setter
    def rule_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_type", value)

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
    @pulumi.getter(name="replacementPattern")
    def replacement_pattern(self) -> Optional[pulumi.Input[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "replacement_pattern")

    @replacement_pattern.setter
    def replacement_pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replacement_pattern", value)

    @property
    @pulumi.getter(name="ruleRegex")
    def rule_regex(self) -> Optional[pulumi.Input[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "rule_regex")

    @rule_regex.setter
    def rule_regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_regex", value)

    @property
    @pulumi.getter(name="ruleVarName")
    def rule_var_name(self) -> Optional[pulumi.Input[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "rule_var_name")

    @rule_var_name.setter
    def rule_var_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_var_name", value)


@pulumi.input_type
class _DevobsDataMaskingState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 replacement_pattern: Optional[pulumi.Input[str]] = None,
                 replacement_type: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 rule_regex: Optional[pulumi.Input[str]] = None,
                 rule_type: Optional[pulumi.Input[str]] = None,
                 rule_var_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DevobsDataMasking resources.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] replacement_pattern: no documentation available
        :param pulumi.Input[str] replacement_type: Possible Values: `SHA256`, `STRING`
        :param pulumi.Input[str] rule_name: Rule Name
        :param pulumi.Input[str] rule_regex: no documentation available
        :param pulumi.Input[str] rule_type: Possible Values: `REGEX`, `VAR_NAME`
        :param pulumi.Input[str] rule_var_name: no documentation available
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if insert_after is not None:
            pulumi.set(__self__, "insert_after", insert_after)
        if replacement_pattern is not None:
            pulumi.set(__self__, "replacement_pattern", replacement_pattern)
        if replacement_type is not None:
            pulumi.set(__self__, "replacement_type", replacement_type)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)
        if rule_regex is not None:
            pulumi.set(__self__, "rule_regex", rule_regex)
        if rule_type is not None:
            pulumi.set(__self__, "rule_type", rule_type)
        if rule_var_name is not None:
            pulumi.set(__self__, "rule_var_name", rule_var_name)

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
    @pulumi.getter(name="replacementPattern")
    def replacement_pattern(self) -> Optional[pulumi.Input[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "replacement_pattern")

    @replacement_pattern.setter
    def replacement_pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replacement_pattern", value)

    @property
    @pulumi.getter(name="replacementType")
    def replacement_type(self) -> Optional[pulumi.Input[str]]:
        """
        Possible Values: `SHA256`, `STRING`
        """
        return pulumi.get(self, "replacement_type")

    @replacement_type.setter
    def replacement_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replacement_type", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Rule Name
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter(name="ruleRegex")
    def rule_regex(self) -> Optional[pulumi.Input[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "rule_regex")

    @rule_regex.setter
    def rule_regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_regex", value)

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> Optional[pulumi.Input[str]]:
        """
        Possible Values: `REGEX`, `VAR_NAME`
        """
        return pulumi.get(self, "rule_type")

    @rule_type.setter
    def rule_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_type", value)

    @property
    @pulumi.getter(name="ruleVarName")
    def rule_var_name(self) -> Optional[pulumi.Input[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "rule_var_name")

    @rule_var_name.setter
    def rule_var_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_var_name", value)


class DevobsDataMasking(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 replacement_pattern: Optional[pulumi.Input[str]] = None,
                 replacement_type: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 rule_regex: Optional[pulumi.Input[str]] = None,
                 rule_type: Optional[pulumi.Input[str]] = None,
                 rule_var_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DevobsDataMasking resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] replacement_pattern: no documentation available
        :param pulumi.Input[str] replacement_type: Possible Values: `SHA256`, `STRING`
        :param pulumi.Input[str] rule_name: Rule Name
        :param pulumi.Input[str] rule_regex: no documentation available
        :param pulumi.Input[str] rule_type: Possible Values: `REGEX`, `VAR_NAME`
        :param pulumi.Input[str] rule_var_name: no documentation available
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DevobsDataMaskingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DevobsDataMasking resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DevobsDataMaskingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DevobsDataMaskingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 replacement_pattern: Optional[pulumi.Input[str]] = None,
                 replacement_type: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 rule_regex: Optional[pulumi.Input[str]] = None,
                 rule_type: Optional[pulumi.Input[str]] = None,
                 rule_var_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DevobsDataMaskingArgs.__new__(DevobsDataMaskingArgs)

            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["insert_after"] = insert_after
            __props__.__dict__["replacement_pattern"] = replacement_pattern
            if replacement_type is None and not opts.urn:
                raise TypeError("Missing required property 'replacement_type'")
            __props__.__dict__["replacement_type"] = replacement_type
            if rule_name is None and not opts.urn:
                raise TypeError("Missing required property 'rule_name'")
            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["rule_regex"] = rule_regex
            if rule_type is None and not opts.urn:
                raise TypeError("Missing required property 'rule_type'")
            __props__.__dict__["rule_type"] = rule_type
            __props__.__dict__["rule_var_name"] = rule_var_name
        super(DevobsDataMasking, __self__).__init__(
            'dynatrace:index/devobsDataMasking:DevobsDataMasking',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            insert_after: Optional[pulumi.Input[str]] = None,
            replacement_pattern: Optional[pulumi.Input[str]] = None,
            replacement_type: Optional[pulumi.Input[str]] = None,
            rule_name: Optional[pulumi.Input[str]] = None,
            rule_regex: Optional[pulumi.Input[str]] = None,
            rule_type: Optional[pulumi.Input[str]] = None,
            rule_var_name: Optional[pulumi.Input[str]] = None) -> 'DevobsDataMasking':
        """
        Get an existing DevobsDataMasking resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] replacement_pattern: no documentation available
        :param pulumi.Input[str] replacement_type: Possible Values: `SHA256`, `STRING`
        :param pulumi.Input[str] rule_name: Rule Name
        :param pulumi.Input[str] rule_regex: no documentation available
        :param pulumi.Input[str] rule_type: Possible Values: `REGEX`, `VAR_NAME`
        :param pulumi.Input[str] rule_var_name: no documentation available
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DevobsDataMaskingState.__new__(_DevobsDataMaskingState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["insert_after"] = insert_after
        __props__.__dict__["replacement_pattern"] = replacement_pattern
        __props__.__dict__["replacement_type"] = replacement_type
        __props__.__dict__["rule_name"] = rule_name
        __props__.__dict__["rule_regex"] = rule_regex
        __props__.__dict__["rule_type"] = rule_type
        __props__.__dict__["rule_var_name"] = rule_var_name
        return DevobsDataMasking(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter(name="replacementPattern")
    def replacement_pattern(self) -> pulumi.Output[Optional[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "replacement_pattern")

    @property
    @pulumi.getter(name="replacementType")
    def replacement_type(self) -> pulumi.Output[str]:
        """
        Possible Values: `SHA256`, `STRING`
        """
        return pulumi.get(self, "replacement_type")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[str]:
        """
        Rule Name
        """
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="ruleRegex")
    def rule_regex(self) -> pulumi.Output[Optional[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "rule_regex")

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Output[str]:
        """
        Possible Values: `REGEX`, `VAR_NAME`
        """
        return pulumi.get(self, "rule_type")

    @property
    @pulumi.getter(name="ruleVarName")
    def rule_var_name(self) -> pulumi.Output[Optional[str]]:
        """
        no documentation available
        """
        return pulumi.get(self, "rule_var_name")

