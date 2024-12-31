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

__all__ = ['GitlabConnectionArgs', 'GitlabConnection']

@pulumi.input_type
class GitlabConnectionArgs:
    def __init__(__self__, *,
                 token: pulumi.Input[str],
                 url: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GitlabConnection resource.
        :param pulumi.Input[str] token: The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.
        :param pulumi.Input[str] url: The GitLab URL instance you want to connect. For example, https://gitlab.com
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name to your GitLab instance.
        """
        pulumi.set(__self__, "token", token)
        pulumi.set(__self__, "url", url)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        """
        The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The GitLab URL instance you want to connect. For example, https://gitlab.com
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique and clearly identifiable connection name to your GitLab instance.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _GitlabConnectionState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GitlabConnection resources.
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name to your GitLab instance.
        :param pulumi.Input[str] token: The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.
        :param pulumi.Input[str] url: The GitLab URL instance you want to connect. For example, https://gitlab.com
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique and clearly identifiable connection name to your GitLab instance.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The GitLab URL instance you want to connect. For example, https://gitlab.com
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class GitlabConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a GitlabConnection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name to your GitLab instance.
        :param pulumi.Input[str] token: The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.
        :param pulumi.Input[str] url: The GitLab URL instance you want to connect. For example, https://gitlab.com
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GitlabConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a GitlabConnection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param GitlabConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GitlabConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GitlabConnectionArgs.__new__(GitlabConnectionArgs)

            __props__.__dict__["name"] = name
            if token is None and not opts.urn:
                raise TypeError("Missing required property 'token'")
            __props__.__dict__["token"] = None if token is None else pulumi.Output.secret(token)
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(GitlabConnection, __self__).__init__(
            'dynatrace:index/gitlabConnection:GitlabConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'GitlabConnection':
        """
        Get an existing GitlabConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique and clearly identifiable connection name to your GitLab instance.
        :param pulumi.Input[str] token: The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.
        :param pulumi.Input[str] url: The GitLab URL instance you want to connect. For example, https://gitlab.com
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GitlabConnectionState.__new__(_GitlabConnectionState)

        __props__.__dict__["name"] = name
        __props__.__dict__["token"] = token
        __props__.__dict__["url"] = url
        return GitlabConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique and clearly identifiable connection name to your GitLab instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The GitLab URL instance you want to connect. For example, https://gitlab.com
        """
        return pulumi.get(self, "url")

