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

__all__ = ['EventDrivenAnsibleConnectionsArgs', 'EventDrivenAnsibleConnections']

@pulumi.input_type
class EventDrivenAnsibleConnectionsArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 url: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EventDrivenAnsibleConnections resource.
        :param pulumi.Input[str] type: Possible Values: `Api_token`
        :param pulumi.Input[str] url: URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name.
        :param pulumi.Input[str] token: API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "url", url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Possible Values: `Api_token`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique and clearly identifiable connection name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


@pulumi.input_type
class _EventDrivenAnsibleConnectionsState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EventDrivenAnsibleConnections resources.
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name.
        :param pulumi.Input[str] token: API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.
        :param pulumi.Input[str] type: Possible Values: `Api_token`
        :param pulumi.Input[str] url: URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique and clearly identifiable connection name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Possible Values: `Api_token`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class EventDrivenAnsibleConnections(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a EventDrivenAnsibleConnections resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name.
        :param pulumi.Input[str] token: API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.
        :param pulumi.Input[str] type: Possible Values: `Api_token`
        :param pulumi.Input[str] url: URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventDrivenAnsibleConnectionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a EventDrivenAnsibleConnections resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param EventDrivenAnsibleConnectionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventDrivenAnsibleConnectionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventDrivenAnsibleConnectionsArgs.__new__(EventDrivenAnsibleConnectionsArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["token"] = None if token is None else pulumi.Output.secret(token)
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(EventDrivenAnsibleConnections, __self__).__init__(
            'dynatrace:index/eventDrivenAnsibleConnections:EventDrivenAnsibleConnections',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'EventDrivenAnsibleConnections':
        """
        Get an existing EventDrivenAnsibleConnections resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name.
        :param pulumi.Input[str] token: API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.
        :param pulumi.Input[str] type: Possible Values: `Api_token`
        :param pulumi.Input[str] url: URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EventDrivenAnsibleConnectionsState.__new__(_EventDrivenAnsibleConnectionsState)

        __props__.__dict__["name"] = name
        __props__.__dict__["token"] = token
        __props__.__dict__["type"] = type
        __props__.__dict__["url"] = url
        return EventDrivenAnsibleConnections(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique and clearly identifiable connection name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Possible Values: `Api_token`
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010
        """
        return pulumi.get(self, "url")

