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

__all__ = ['MobileAppRequestErrorsArgs', 'MobileAppRequestErrors']

@pulumi.input_type
class MobileAppRequestErrorsArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 error_rules: Optional[pulumi.Input['MobileAppRequestErrorsErrorRulesArgs']] = None):
        """
        The set of arguments for constructing a MobileAppRequestErrors resource.
        :param pulumi.Input[str] scope: The scope of this setting (MOBILE*APPLICATION, CUSTOM*APPLICATION)
        :param pulumi.Input['MobileAppRequestErrorsErrorRulesArgs'] error_rules: no documentation available
        """
        pulumi.set(__self__, "scope", scope)
        if error_rules is not None:
            pulumi.set(__self__, "error_rules", error_rules)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of this setting (MOBILE*APPLICATION, CUSTOM*APPLICATION)
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="errorRules")
    def error_rules(self) -> Optional[pulumi.Input['MobileAppRequestErrorsErrorRulesArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "error_rules")

    @error_rules.setter
    def error_rules(self, value: Optional[pulumi.Input['MobileAppRequestErrorsErrorRulesArgs']]):
        pulumi.set(self, "error_rules", value)


@pulumi.input_type
class _MobileAppRequestErrorsState:
    def __init__(__self__, *,
                 error_rules: Optional[pulumi.Input['MobileAppRequestErrorsErrorRulesArgs']] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MobileAppRequestErrors resources.
        :param pulumi.Input['MobileAppRequestErrorsErrorRulesArgs'] error_rules: no documentation available
        :param pulumi.Input[str] scope: The scope of this setting (MOBILE*APPLICATION, CUSTOM*APPLICATION)
        """
        if error_rules is not None:
            pulumi.set(__self__, "error_rules", error_rules)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter(name="errorRules")
    def error_rules(self) -> Optional[pulumi.Input['MobileAppRequestErrorsErrorRulesArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "error_rules")

    @error_rules.setter
    def error_rules(self, value: Optional[pulumi.Input['MobileAppRequestErrorsErrorRulesArgs']]):
        pulumi.set(self, "error_rules", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this setting (MOBILE*APPLICATION, CUSTOM*APPLICATION)
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class MobileAppRequestErrors(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 error_rules: Optional[pulumi.Input[Union['MobileAppRequestErrorsErrorRulesArgs', 'MobileAppRequestErrorsErrorRulesArgsDict']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a MobileAppRequestErrors resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['MobileAppRequestErrorsErrorRulesArgs', 'MobileAppRequestErrorsErrorRulesArgsDict']] error_rules: no documentation available
        :param pulumi.Input[str] scope: The scope of this setting (MOBILE*APPLICATION, CUSTOM*APPLICATION)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MobileAppRequestErrorsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MobileAppRequestErrors resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MobileAppRequestErrorsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MobileAppRequestErrorsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 error_rules: Optional[pulumi.Input[Union['MobileAppRequestErrorsErrorRulesArgs', 'MobileAppRequestErrorsErrorRulesArgsDict']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MobileAppRequestErrorsArgs.__new__(MobileAppRequestErrorsArgs)

            __props__.__dict__["error_rules"] = error_rules
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
        super(MobileAppRequestErrors, __self__).__init__(
            'dynatrace:index/mobileAppRequestErrors:MobileAppRequestErrors',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            error_rules: Optional[pulumi.Input[Union['MobileAppRequestErrorsErrorRulesArgs', 'MobileAppRequestErrorsErrorRulesArgsDict']]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'MobileAppRequestErrors':
        """
        Get an existing MobileAppRequestErrors resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['MobileAppRequestErrorsErrorRulesArgs', 'MobileAppRequestErrorsErrorRulesArgsDict']] error_rules: no documentation available
        :param pulumi.Input[str] scope: The scope of this setting (MOBILE*APPLICATION, CUSTOM*APPLICATION)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MobileAppRequestErrorsState.__new__(_MobileAppRequestErrorsState)

        __props__.__dict__["error_rules"] = error_rules
        __props__.__dict__["scope"] = scope
        return MobileAppRequestErrors(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="errorRules")
    def error_rules(self) -> pulumi.Output[Optional['outputs.MobileAppRequestErrorsErrorRules']]:
        """
        no documentation available
        """
        return pulumi.get(self, "error_rules")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The scope of this setting (MOBILE*APPLICATION, CUSTOM*APPLICATION)
        """
        return pulumi.get(self, "scope")

