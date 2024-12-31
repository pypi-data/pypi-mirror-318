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

__all__ = ['WebAppCustomConfigPropertiesArgs', 'WebAppCustomConfigProperties']

@pulumi.input_type
class WebAppCustomConfigPropertiesArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 custom_property: pulumi.Input[str]):
        """
        The set of arguments for constructing a WebAppCustomConfigProperties resource.
        :param pulumi.Input[str] application_id: The scope of this setting
        :param pulumi.Input[str] custom_property: Custom configuration property
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "custom_property", custom_property)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        """
        The scope of this setting
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="customProperty")
    def custom_property(self) -> pulumi.Input[str]:
        """
        Custom configuration property
        """
        return pulumi.get(self, "custom_property")

    @custom_property.setter
    def custom_property(self, value: pulumi.Input[str]):
        pulumi.set(self, "custom_property", value)


@pulumi.input_type
class _WebAppCustomConfigPropertiesState:
    def __init__(__self__, *,
                 application_id: Optional[pulumi.Input[str]] = None,
                 custom_property: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WebAppCustomConfigProperties resources.
        :param pulumi.Input[str] application_id: The scope of this setting
        :param pulumi.Input[str] custom_property: Custom configuration property
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if custom_property is not None:
            pulumi.set(__self__, "custom_property", custom_property)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this setting
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="customProperty")
    def custom_property(self) -> Optional[pulumi.Input[str]]:
        """
        Custom configuration property
        """
        return pulumi.get(self, "custom_property")

    @custom_property.setter
    def custom_property(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_property", value)


class WebAppCustomConfigProperties(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 custom_property: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a WebAppCustomConfigProperties resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The scope of this setting
        :param pulumi.Input[str] custom_property: Custom configuration property
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppCustomConfigPropertiesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a WebAppCustomConfigProperties resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param WebAppCustomConfigPropertiesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppCustomConfigPropertiesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 custom_property: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebAppCustomConfigPropertiesArgs.__new__(WebAppCustomConfigPropertiesArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            if custom_property is None and not opts.urn:
                raise TypeError("Missing required property 'custom_property'")
            __props__.__dict__["custom_property"] = custom_property
        super(WebAppCustomConfigProperties, __self__).__init__(
            'dynatrace:index/webAppCustomConfigProperties:WebAppCustomConfigProperties',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            custom_property: Optional[pulumi.Input[str]] = None) -> 'WebAppCustomConfigProperties':
        """
        Get an existing WebAppCustomConfigProperties resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The scope of this setting
        :param pulumi.Input[str] custom_property: Custom configuration property
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WebAppCustomConfigPropertiesState.__new__(_WebAppCustomConfigPropertiesState)

        __props__.__dict__["application_id"] = application_id
        __props__.__dict__["custom_property"] = custom_property
        return WebAppCustomConfigProperties(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The scope of this setting
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="customProperty")
    def custom_property(self) -> pulumi.Output[str]:
        """
        Custom configuration property
        """
        return pulumi.get(self, "custom_property")

