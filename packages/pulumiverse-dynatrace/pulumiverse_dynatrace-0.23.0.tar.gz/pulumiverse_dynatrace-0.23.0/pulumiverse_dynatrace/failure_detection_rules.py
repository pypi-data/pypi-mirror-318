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

__all__ = ['FailureDetectionRulesArgs', 'FailureDetectionRules']

@pulumi.input_type
class FailureDetectionRulesArgs:
    def __init__(__self__, *,
                 conditions: pulumi.Input['FailureDetectionRulesConditionsArgs'],
                 enabled: pulumi.Input[bool],
                 parameter_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FailureDetectionRules resource.
        :param pulumi.Input['FailureDetectionRulesConditionsArgs'] conditions: Conditions
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] parameter_id: Failure detection parameters
        :param pulumi.Input[str] description: Rule description
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] name: Rule name
        """
        pulumi.set(__self__, "conditions", conditions)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "parameter_id", parameter_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if insert_after is not None:
            pulumi.set(__self__, "insert_after", insert_after)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Input['FailureDetectionRulesConditionsArgs']:
        """
        Conditions
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: pulumi.Input['FailureDetectionRulesConditionsArgs']):
        pulumi.set(self, "conditions", value)

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
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> pulumi.Input[str]:
        """
        Failure detection parameters
        """
        return pulumi.get(self, "parameter_id")

    @parameter_id.setter
    def parameter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Rule description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Rule name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FailureDetectionRulesState:
    def __init__(__self__, *,
                 conditions: Optional[pulumi.Input['FailureDetectionRulesConditionsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameter_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FailureDetectionRules resources.
        :param pulumi.Input['FailureDetectionRulesConditionsArgs'] conditions: Conditions
        :param pulumi.Input[str] description: Rule description
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] name: Rule name
        :param pulumi.Input[str] parameter_id: Failure detection parameters
        """
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if insert_after is not None:
            pulumi.set(__self__, "insert_after", insert_after)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameter_id is not None:
            pulumi.set(__self__, "parameter_id", parameter_id)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input['FailureDetectionRulesConditionsArgs']]:
        """
        Conditions
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input['FailureDetectionRulesConditionsArgs']]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Rule description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Rule name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> Optional[pulumi.Input[str]]:
        """
        Failure detection parameters
        """
        return pulumi.get(self, "parameter_id")

    @parameter_id.setter
    def parameter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_id", value)


class FailureDetectionRules(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conditions: Optional[pulumi.Input[Union['FailureDetectionRulesConditionsArgs', 'FailureDetectionRulesConditionsArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameter_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a FailureDetectionRules resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['FailureDetectionRulesConditionsArgs', 'FailureDetectionRulesConditionsArgsDict']] conditions: Conditions
        :param pulumi.Input[str] description: Rule description
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] name: Rule name
        :param pulumi.Input[str] parameter_id: Failure detection parameters
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FailureDetectionRulesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a FailureDetectionRules resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param FailureDetectionRulesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FailureDetectionRulesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 conditions: Optional[pulumi.Input[Union['FailureDetectionRulesConditionsArgs', 'FailureDetectionRulesConditionsArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 insert_after: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameter_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FailureDetectionRulesArgs.__new__(FailureDetectionRulesArgs)

            if conditions is None and not opts.urn:
                raise TypeError("Missing required property 'conditions'")
            __props__.__dict__["conditions"] = conditions
            __props__.__dict__["description"] = description
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["insert_after"] = insert_after
            __props__.__dict__["name"] = name
            if parameter_id is None and not opts.urn:
                raise TypeError("Missing required property 'parameter_id'")
            __props__.__dict__["parameter_id"] = parameter_id
        super(FailureDetectionRules, __self__).__init__(
            'dynatrace:index/failureDetectionRules:FailureDetectionRules',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            conditions: Optional[pulumi.Input[Union['FailureDetectionRulesConditionsArgs', 'FailureDetectionRulesConditionsArgsDict']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            insert_after: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameter_id: Optional[pulumi.Input[str]] = None) -> 'FailureDetectionRules':
        """
        Get an existing FailureDetectionRules resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['FailureDetectionRulesConditionsArgs', 'FailureDetectionRulesConditionsArgsDict']] conditions: Conditions
        :param pulumi.Input[str] description: Rule description
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] insert_after: Because this resource allows for ordering you may specify the ID of the resource instance that comes before this instance regarding order. If not specified when creating the setting will be added to the end of the list. If not specified during update the order will remain untouched
        :param pulumi.Input[str] name: Rule name
        :param pulumi.Input[str] parameter_id: Failure detection parameters
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FailureDetectionRulesState.__new__(_FailureDetectionRulesState)

        __props__.__dict__["conditions"] = conditions
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["insert_after"] = insert_after
        __props__.__dict__["name"] = name
        __props__.__dict__["parameter_id"] = parameter_id
        return FailureDetectionRules(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output['outputs.FailureDetectionRulesConditions']:
        """
        Conditions
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Rule description
        """
        return pulumi.get(self, "description")

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
    def name(self) -> pulumi.Output[str]:
        """
        Rule name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> pulumi.Output[str]:
        """
        Failure detection parameters
        """
        return pulumi.get(self, "parameter_id")

