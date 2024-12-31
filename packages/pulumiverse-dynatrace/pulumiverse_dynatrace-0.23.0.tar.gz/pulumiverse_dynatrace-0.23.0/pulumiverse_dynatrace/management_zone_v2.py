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

__all__ = ['ManagementZoneV2Args', 'ManagementZoneV2']

@pulumi.input_type
class ManagementZoneV2Args:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 legacy_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input['ManagementZoneV2RulesArgs']] = None):
        """
        The set of arguments for constructing a ManagementZoneV2 resource.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] legacy_id: The ID of this setting when referred to by the Config REST API V1
        :param pulumi.Input[str] name: **Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!
        :param pulumi.Input['ManagementZoneV2RulesArgs'] rules: Rules
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if legacy_id is not None:
            pulumi.set(__self__, "legacy_id", legacy_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="legacyId")
    def legacy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of this setting when referred to by the Config REST API V1
        """
        return pulumi.get(self, "legacy_id")

    @legacy_id.setter
    def legacy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "legacy_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        **Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input['ManagementZoneV2RulesArgs']]:
        """
        Rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input['ManagementZoneV2RulesArgs']]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class _ManagementZoneV2State:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 legacy_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input['ManagementZoneV2RulesArgs']] = None):
        """
        Input properties used for looking up and filtering ManagementZoneV2 resources.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] legacy_id: The ID of this setting when referred to by the Config REST API V1
        :param pulumi.Input[str] name: **Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!
        :param pulumi.Input['ManagementZoneV2RulesArgs'] rules: Rules
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if legacy_id is not None:
            pulumi.set(__self__, "legacy_id", legacy_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="legacyId")
    def legacy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of this setting when referred to by the Config REST API V1
        """
        return pulumi.get(self, "legacy_id")

    @legacy_id.setter
    def legacy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "legacy_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        **Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input['ManagementZoneV2RulesArgs']]:
        """
        Rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input['ManagementZoneV2RulesArgs']]):
        pulumi.set(self, "rules", value)


class ManagementZoneV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 legacy_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Union['ManagementZoneV2RulesArgs', 'ManagementZoneV2RulesArgsDict']]] = None,
                 __props__=None):
        """
        Create a ManagementZoneV2 resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] legacy_id: The ID of this setting when referred to by the Config REST API V1
        :param pulumi.Input[str] name: **Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!
        :param pulumi.Input[Union['ManagementZoneV2RulesArgs', 'ManagementZoneV2RulesArgsDict']] rules: Rules
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ManagementZoneV2Args] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ManagementZoneV2 resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ManagementZoneV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementZoneV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 legacy_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Union['ManagementZoneV2RulesArgs', 'ManagementZoneV2RulesArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagementZoneV2Args.__new__(ManagementZoneV2Args)

            __props__.__dict__["description"] = description
            __props__.__dict__["legacy_id"] = legacy_id
            __props__.__dict__["name"] = name
            __props__.__dict__["rules"] = rules
        super(ManagementZoneV2, __self__).__init__(
            'dynatrace:index/managementZoneV2:ManagementZoneV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            legacy_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Union['ManagementZoneV2RulesArgs', 'ManagementZoneV2RulesArgsDict']]] = None) -> 'ManagementZoneV2':
        """
        Get an existing ManagementZoneV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description
        :param pulumi.Input[str] legacy_id: The ID of this setting when referred to by the Config REST API V1
        :param pulumi.Input[str] name: **Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!
        :param pulumi.Input[Union['ManagementZoneV2RulesArgs', 'ManagementZoneV2RulesArgsDict']] rules: Rules
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagementZoneV2State.__new__(_ManagementZoneV2State)

        __props__.__dict__["description"] = description
        __props__.__dict__["legacy_id"] = legacy_id
        __props__.__dict__["name"] = name
        __props__.__dict__["rules"] = rules
        return ManagementZoneV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="legacyId")
    def legacy_id(self) -> pulumi.Output[str]:
        """
        The ID of this setting when referred to by the Config REST API V1
        """
        return pulumi.get(self, "legacy_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        **Be careful when renaming** - if there are policies that are referencing this Management zone, they will need to be adapted to the new name!
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional['outputs.ManagementZoneV2Rules']]:
        """
        Rules
        """
        return pulumi.get(self, "rules")

