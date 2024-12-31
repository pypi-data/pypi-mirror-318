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

__all__ = ['KeyUserActionArgs', 'KeyUserAction']

@pulumi.input_type
class KeyUserActionArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KeyUserAction resource.
        :param pulumi.Input[str] application_id: The ID of the WebApplication
        :param pulumi.Input[str] type: The type of the action. Possible values are `Custom`, `Load` and `Xhr`
        :param pulumi.Input[str] domain: The domain where the action is performed
        :param pulumi.Input[str] name: The name of the action
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "type", type)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        """
        The ID of the WebApplication
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the action. Possible values are `Custom`, `Load` and `Xhr`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain where the action is performed
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the action
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _KeyUserActionState:
    def __init__(__self__, *,
                 application_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KeyUserAction resources.
        :param pulumi.Input[str] application_id: The ID of the WebApplication
        :param pulumi.Input[str] domain: The domain where the action is performed
        :param pulumi.Input[str] name: The name of the action
        :param pulumi.Input[str] type: The type of the action. Possible values are `Custom`, `Load` and `Xhr`
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the WebApplication
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain where the action is performed
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the action
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the action. Possible values are `Custom`, `Load` and `Xhr`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class KeyUserAction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a KeyUserAction resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The ID of the WebApplication
        :param pulumi.Input[str] domain: The domain where the action is performed
        :param pulumi.Input[str] name: The name of the action
        :param pulumi.Input[str] type: The type of the action. Possible values are `Custom`, `Load` and `Xhr`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeyUserActionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a KeyUserAction resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KeyUserActionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyUserActionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeyUserActionArgs.__new__(KeyUserActionArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["domain"] = domain
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(KeyUserAction, __self__).__init__(
            'dynatrace:index/keyUserAction:KeyUserAction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'KeyUserAction':
        """
        Get an existing KeyUserAction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The ID of the WebApplication
        :param pulumi.Input[str] domain: The domain where the action is performed
        :param pulumi.Input[str] name: The name of the action
        :param pulumi.Input[str] type: The type of the action. Possible values are `Custom`, `Load` and `Xhr`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KeyUserActionState.__new__(_KeyUserActionState)

        __props__.__dict__["application_id"] = application_id
        __props__.__dict__["domain"] = domain
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        return KeyUserAction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The ID of the WebApplication
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        """
        The domain where the action is performed
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the action
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the action. Possible values are `Custom`, `Load` and `Xhr`
        """
        return pulumi.get(self, "type")

