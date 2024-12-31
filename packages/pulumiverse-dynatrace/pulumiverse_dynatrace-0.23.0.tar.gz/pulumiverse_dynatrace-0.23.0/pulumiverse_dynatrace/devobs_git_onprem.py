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

__all__ = ['DevobsGitOnpremArgs', 'DevobsGitOnprem']

@pulumi.input_type
class DevobsGitOnpremArgs:
    def __init__(__self__, *,
                 git_provider: pulumi.Input[str],
                 url: pulumi.Input[str],
                 include_credentials: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a DevobsGitOnprem resource.
        :param pulumi.Input[str] git_provider: Possible Values: `AzureOnPrem`, `BitbucketOnPrem`, `GithubOnPrem`, `GitlabOnPrem`
        :param pulumi.Input[str] url: An HTTP/HTTPS URL of your server
        :param pulumi.Input[bool] include_credentials: If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.
        """
        pulumi.set(__self__, "git_provider", git_provider)
        pulumi.set(__self__, "url", url)
        if include_credentials is not None:
            pulumi.set(__self__, "include_credentials", include_credentials)

    @property
    @pulumi.getter(name="gitProvider")
    def git_provider(self) -> pulumi.Input[str]:
        """
        Possible Values: `AzureOnPrem`, `BitbucketOnPrem`, `GithubOnPrem`, `GitlabOnPrem`
        """
        return pulumi.get(self, "git_provider")

    @git_provider.setter
    def git_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "git_provider", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        An HTTP/HTTPS URL of your server
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="includeCredentials")
    def include_credentials(self) -> Optional[pulumi.Input[bool]]:
        """
        If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.
        """
        return pulumi.get(self, "include_credentials")

    @include_credentials.setter
    def include_credentials(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_credentials", value)


@pulumi.input_type
class _DevobsGitOnpremState:
    def __init__(__self__, *,
                 git_provider: Optional[pulumi.Input[str]] = None,
                 include_credentials: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DevobsGitOnprem resources.
        :param pulumi.Input[str] git_provider: Possible Values: `AzureOnPrem`, `BitbucketOnPrem`, `GithubOnPrem`, `GitlabOnPrem`
        :param pulumi.Input[bool] include_credentials: If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.
        :param pulumi.Input[str] url: An HTTP/HTTPS URL of your server
        """
        if git_provider is not None:
            pulumi.set(__self__, "git_provider", git_provider)
        if include_credentials is not None:
            pulumi.set(__self__, "include_credentials", include_credentials)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="gitProvider")
    def git_provider(self) -> Optional[pulumi.Input[str]]:
        """
        Possible Values: `AzureOnPrem`, `BitbucketOnPrem`, `GithubOnPrem`, `GitlabOnPrem`
        """
        return pulumi.get(self, "git_provider")

    @git_provider.setter
    def git_provider(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "git_provider", value)

    @property
    @pulumi.getter(name="includeCredentials")
    def include_credentials(self) -> Optional[pulumi.Input[bool]]:
        """
        If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.
        """
        return pulumi.get(self, "include_credentials")

    @include_credentials.setter
    def include_credentials(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_credentials", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        An HTTP/HTTPS URL of your server
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class DevobsGitOnprem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 git_provider: Optional[pulumi.Input[str]] = None,
                 include_credentials: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DevobsGitOnprem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] git_provider: Possible Values: `AzureOnPrem`, `BitbucketOnPrem`, `GithubOnPrem`, `GitlabOnPrem`
        :param pulumi.Input[bool] include_credentials: If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.
        :param pulumi.Input[str] url: An HTTP/HTTPS URL of your server
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DevobsGitOnpremArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DevobsGitOnprem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DevobsGitOnpremArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DevobsGitOnpremArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 git_provider: Optional[pulumi.Input[str]] = None,
                 include_credentials: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DevobsGitOnpremArgs.__new__(DevobsGitOnpremArgs)

            if git_provider is None and not opts.urn:
                raise TypeError("Missing required property 'git_provider'")
            __props__.__dict__["git_provider"] = git_provider
            __props__.__dict__["include_credentials"] = include_credentials
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
        super(DevobsGitOnprem, __self__).__init__(
            'dynatrace:index/devobsGitOnprem:DevobsGitOnprem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            git_provider: Optional[pulumi.Input[str]] = None,
            include_credentials: Optional[pulumi.Input[bool]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'DevobsGitOnprem':
        """
        Get an existing DevobsGitOnprem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] git_provider: Possible Values: `AzureOnPrem`, `BitbucketOnPrem`, `GithubOnPrem`, `GitlabOnPrem`
        :param pulumi.Input[bool] include_credentials: If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.
        :param pulumi.Input[str] url: An HTTP/HTTPS URL of your server
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DevobsGitOnpremState.__new__(_DevobsGitOnpremState)

        __props__.__dict__["git_provider"] = git_provider
        __props__.__dict__["include_credentials"] = include_credentials
        __props__.__dict__["url"] = url
        return DevobsGitOnprem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="gitProvider")
    def git_provider(self) -> pulumi.Output[str]:
        """
        Possible Values: `AzureOnPrem`, `BitbucketOnPrem`, `GithubOnPrem`, `GitlabOnPrem`
        """
        return pulumi.get(self, "git_provider")

    @property
    @pulumi.getter(name="includeCredentials")
    def include_credentials(self) -> pulumi.Output[Optional[bool]]:
        """
        If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.
        """
        return pulumi.get(self, "include_credentials")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        An HTTP/HTTPS URL of your server
        """
        return pulumi.get(self, "url")

