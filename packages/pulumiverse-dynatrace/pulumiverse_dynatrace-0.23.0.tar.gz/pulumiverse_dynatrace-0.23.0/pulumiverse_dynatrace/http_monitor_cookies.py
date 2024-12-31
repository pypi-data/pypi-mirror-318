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

__all__ = ['HttpMonitorCookiesArgs', 'HttpMonitorCookies']

@pulumi.input_type
class HttpMonitorCookiesArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 scope: pulumi.Input[str],
                 cookies: Optional[pulumi.Input['HttpMonitorCookiesCookiesArgs']] = None):
        """
        The set of arguments for constructing a HttpMonitorCookies resource.
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] scope: The scope of this setting (HTTP_CHECK)
        :param pulumi.Input['HttpMonitorCookiesCookiesArgs'] cookies: no documentation available
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "scope", scope)
        if cookies is not None:
            pulumi.set(__self__, "cookies", cookies)

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
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of this setting (HTTP_CHECK)
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def cookies(self) -> Optional[pulumi.Input['HttpMonitorCookiesCookiesArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "cookies")

    @cookies.setter
    def cookies(self, value: Optional[pulumi.Input['HttpMonitorCookiesCookiesArgs']]):
        pulumi.set(self, "cookies", value)


@pulumi.input_type
class _HttpMonitorCookiesState:
    def __init__(__self__, *,
                 cookies: Optional[pulumi.Input['HttpMonitorCookiesCookiesArgs']] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HttpMonitorCookies resources.
        :param pulumi.Input['HttpMonitorCookiesCookiesArgs'] cookies: no documentation available
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] scope: The scope of this setting (HTTP_CHECK)
        """
        if cookies is not None:
            pulumi.set(__self__, "cookies", cookies)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def cookies(self) -> Optional[pulumi.Input['HttpMonitorCookiesCookiesArgs']]:
        """
        no documentation available
        """
        return pulumi.get(self, "cookies")

    @cookies.setter
    def cookies(self, value: Optional[pulumi.Input['HttpMonitorCookiesCookiesArgs']]):
        pulumi.set(self, "cookies", value)

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
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of this setting (HTTP_CHECK)
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class HttpMonitorCookies(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cookies: Optional[pulumi.Input[Union['HttpMonitorCookiesCookiesArgs', 'HttpMonitorCookiesCookiesArgsDict']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a HttpMonitorCookies resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['HttpMonitorCookiesCookiesArgs', 'HttpMonitorCookiesCookiesArgsDict']] cookies: no documentation available
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] scope: The scope of this setting (HTTP_CHECK)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HttpMonitorCookiesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a HttpMonitorCookies resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param HttpMonitorCookiesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HttpMonitorCookiesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cookies: Optional[pulumi.Input[Union['HttpMonitorCookiesCookiesArgs', 'HttpMonitorCookiesCookiesArgsDict']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HttpMonitorCookiesArgs.__new__(HttpMonitorCookiesArgs)

            __props__.__dict__["cookies"] = cookies
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
        super(HttpMonitorCookies, __self__).__init__(
            'dynatrace:index/httpMonitorCookies:HttpMonitorCookies',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cookies: Optional[pulumi.Input[Union['HttpMonitorCookiesCookiesArgs', 'HttpMonitorCookiesCookiesArgsDict']]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'HttpMonitorCookies':
        """
        Get an existing HttpMonitorCookies resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['HttpMonitorCookiesCookiesArgs', 'HttpMonitorCookiesCookiesArgsDict']] cookies: no documentation available
        :param pulumi.Input[bool] enabled: This setting is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] scope: The scope of this setting (HTTP_CHECK)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HttpMonitorCookiesState.__new__(_HttpMonitorCookiesState)

        __props__.__dict__["cookies"] = cookies
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["scope"] = scope
        return HttpMonitorCookies(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cookies(self) -> pulumi.Output[Optional['outputs.HttpMonitorCookiesCookies']]:
        """
        no documentation available
        """
        return pulumi.get(self, "cookies")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        This setting is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The scope of this setting (HTTP_CHECK)
        """
        return pulumi.get(self, "scope")

