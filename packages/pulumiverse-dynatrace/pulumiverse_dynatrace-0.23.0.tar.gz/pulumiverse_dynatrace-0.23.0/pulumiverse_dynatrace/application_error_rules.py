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

__all__ = ['ApplicationErrorRulesArgs', 'ApplicationErrorRules']

@pulumi.input_type
class ApplicationErrorRulesArgs:
    def __init__(__self__, *,
                 custom_errors: Optional[pulumi.Input['ApplicationErrorRulesCustomErrorsArgs']] = None,
                 http_errors: Optional[pulumi.Input['ApplicationErrorRulesHttpErrorsArgs']] = None,
                 ignore_custom_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_http_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_js_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 web_application_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApplicationErrorRules resource.
        :param pulumi.Input['ApplicationErrorRulesCustomErrorsArgs'] custom_errors: (Field has overlap with `WebAppCustomErrors`) An ordered list of HTTP errors.
        :param pulumi.Input['ApplicationErrorRulesHttpErrorsArgs'] http_errors: (Field has overlap with `WebAppRequestErrors`) An ordered list of HTTP errors. Rules are evaluated from top to bottom;
               the first matching rule applies
        :param pulumi.Input[bool] ignore_custom_errors_apdex: (Field has overlap with `WebAppCustomErrors`) Exclude (`true`) or include (`false`) custom errors listed in
               **customErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_http_errors_apdex: (Field has overlap with `WebAppRequestErrors`) Exclude (`true`) or include (`false`) HTTP errors listed in
               **httpErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_js_errors_apdex: Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation
        :param pulumi.Input[str] web_application_id: The EntityID of the the WebApplication
        """
        if custom_errors is not None:
            pulumi.set(__self__, "custom_errors", custom_errors)
        if http_errors is not None:
            pulumi.set(__self__, "http_errors", http_errors)
        if ignore_custom_errors_apdex is not None:
            pulumi.set(__self__, "ignore_custom_errors_apdex", ignore_custom_errors_apdex)
        if ignore_http_errors_apdex is not None:
            pulumi.set(__self__, "ignore_http_errors_apdex", ignore_http_errors_apdex)
        if ignore_js_errors_apdex is not None:
            pulumi.set(__self__, "ignore_js_errors_apdex", ignore_js_errors_apdex)
        if web_application_id is not None:
            pulumi.set(__self__, "web_application_id", web_application_id)

    @property
    @pulumi.getter(name="customErrors")
    def custom_errors(self) -> Optional[pulumi.Input['ApplicationErrorRulesCustomErrorsArgs']]:
        """
        (Field has overlap with `WebAppCustomErrors`) An ordered list of HTTP errors.
        """
        return pulumi.get(self, "custom_errors")

    @custom_errors.setter
    def custom_errors(self, value: Optional[pulumi.Input['ApplicationErrorRulesCustomErrorsArgs']]):
        pulumi.set(self, "custom_errors", value)

    @property
    @pulumi.getter(name="httpErrors")
    def http_errors(self) -> Optional[pulumi.Input['ApplicationErrorRulesHttpErrorsArgs']]:
        """
        (Field has overlap with `WebAppRequestErrors`) An ordered list of HTTP errors. Rules are evaluated from top to bottom;
        the first matching rule applies
        """
        return pulumi.get(self, "http_errors")

    @http_errors.setter
    def http_errors(self, value: Optional[pulumi.Input['ApplicationErrorRulesHttpErrorsArgs']]):
        pulumi.set(self, "http_errors", value)

    @property
    @pulumi.getter(name="ignoreCustomErrorsApdex")
    def ignore_custom_errors_apdex(self) -> Optional[pulumi.Input[bool]]:
        """
        (Field has overlap with `WebAppCustomErrors`) Exclude (`true`) or include (`false`) custom errors listed in
        **customErrorRules** in Apdex calculation
        """
        return pulumi.get(self, "ignore_custom_errors_apdex")

    @ignore_custom_errors_apdex.setter
    def ignore_custom_errors_apdex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_custom_errors_apdex", value)

    @property
    @pulumi.getter(name="ignoreHttpErrorsApdex")
    def ignore_http_errors_apdex(self) -> Optional[pulumi.Input[bool]]:
        """
        (Field has overlap with `WebAppRequestErrors`) Exclude (`true`) or include (`false`) HTTP errors listed in
        **httpErrorRules** in Apdex calculation
        """
        return pulumi.get(self, "ignore_http_errors_apdex")

    @ignore_http_errors_apdex.setter
    def ignore_http_errors_apdex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_http_errors_apdex", value)

    @property
    @pulumi.getter(name="ignoreJsErrorsApdex")
    def ignore_js_errors_apdex(self) -> Optional[pulumi.Input[bool]]:
        """
        Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation
        """
        return pulumi.get(self, "ignore_js_errors_apdex")

    @ignore_js_errors_apdex.setter
    def ignore_js_errors_apdex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_js_errors_apdex", value)

    @property
    @pulumi.getter(name="webApplicationId")
    def web_application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The EntityID of the the WebApplication
        """
        return pulumi.get(self, "web_application_id")

    @web_application_id.setter
    def web_application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_application_id", value)


@pulumi.input_type
class _ApplicationErrorRulesState:
    def __init__(__self__, *,
                 custom_errors: Optional[pulumi.Input['ApplicationErrorRulesCustomErrorsArgs']] = None,
                 http_errors: Optional[pulumi.Input['ApplicationErrorRulesHttpErrorsArgs']] = None,
                 ignore_custom_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_http_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_js_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 web_application_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApplicationErrorRules resources.
        :param pulumi.Input['ApplicationErrorRulesCustomErrorsArgs'] custom_errors: (Field has overlap with `WebAppCustomErrors`) An ordered list of HTTP errors.
        :param pulumi.Input['ApplicationErrorRulesHttpErrorsArgs'] http_errors: (Field has overlap with `WebAppRequestErrors`) An ordered list of HTTP errors. Rules are evaluated from top to bottom;
               the first matching rule applies
        :param pulumi.Input[bool] ignore_custom_errors_apdex: (Field has overlap with `WebAppCustomErrors`) Exclude (`true`) or include (`false`) custom errors listed in
               **customErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_http_errors_apdex: (Field has overlap with `WebAppRequestErrors`) Exclude (`true`) or include (`false`) HTTP errors listed in
               **httpErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_js_errors_apdex: Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation
        :param pulumi.Input[str] web_application_id: The EntityID of the the WebApplication
        """
        if custom_errors is not None:
            pulumi.set(__self__, "custom_errors", custom_errors)
        if http_errors is not None:
            pulumi.set(__self__, "http_errors", http_errors)
        if ignore_custom_errors_apdex is not None:
            pulumi.set(__self__, "ignore_custom_errors_apdex", ignore_custom_errors_apdex)
        if ignore_http_errors_apdex is not None:
            pulumi.set(__self__, "ignore_http_errors_apdex", ignore_http_errors_apdex)
        if ignore_js_errors_apdex is not None:
            pulumi.set(__self__, "ignore_js_errors_apdex", ignore_js_errors_apdex)
        if web_application_id is not None:
            pulumi.set(__self__, "web_application_id", web_application_id)

    @property
    @pulumi.getter(name="customErrors")
    def custom_errors(self) -> Optional[pulumi.Input['ApplicationErrorRulesCustomErrorsArgs']]:
        """
        (Field has overlap with `WebAppCustomErrors`) An ordered list of HTTP errors.
        """
        return pulumi.get(self, "custom_errors")

    @custom_errors.setter
    def custom_errors(self, value: Optional[pulumi.Input['ApplicationErrorRulesCustomErrorsArgs']]):
        pulumi.set(self, "custom_errors", value)

    @property
    @pulumi.getter(name="httpErrors")
    def http_errors(self) -> Optional[pulumi.Input['ApplicationErrorRulesHttpErrorsArgs']]:
        """
        (Field has overlap with `WebAppRequestErrors`) An ordered list of HTTP errors. Rules are evaluated from top to bottom;
        the first matching rule applies
        """
        return pulumi.get(self, "http_errors")

    @http_errors.setter
    def http_errors(self, value: Optional[pulumi.Input['ApplicationErrorRulesHttpErrorsArgs']]):
        pulumi.set(self, "http_errors", value)

    @property
    @pulumi.getter(name="ignoreCustomErrorsApdex")
    def ignore_custom_errors_apdex(self) -> Optional[pulumi.Input[bool]]:
        """
        (Field has overlap with `WebAppCustomErrors`) Exclude (`true`) or include (`false`) custom errors listed in
        **customErrorRules** in Apdex calculation
        """
        return pulumi.get(self, "ignore_custom_errors_apdex")

    @ignore_custom_errors_apdex.setter
    def ignore_custom_errors_apdex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_custom_errors_apdex", value)

    @property
    @pulumi.getter(name="ignoreHttpErrorsApdex")
    def ignore_http_errors_apdex(self) -> Optional[pulumi.Input[bool]]:
        """
        (Field has overlap with `WebAppRequestErrors`) Exclude (`true`) or include (`false`) HTTP errors listed in
        **httpErrorRules** in Apdex calculation
        """
        return pulumi.get(self, "ignore_http_errors_apdex")

    @ignore_http_errors_apdex.setter
    def ignore_http_errors_apdex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_http_errors_apdex", value)

    @property
    @pulumi.getter(name="ignoreJsErrorsApdex")
    def ignore_js_errors_apdex(self) -> Optional[pulumi.Input[bool]]:
        """
        Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation
        """
        return pulumi.get(self, "ignore_js_errors_apdex")

    @ignore_js_errors_apdex.setter
    def ignore_js_errors_apdex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_js_errors_apdex", value)

    @property
    @pulumi.getter(name="webApplicationId")
    def web_application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The EntityID of the the WebApplication
        """
        return pulumi.get(self, "web_application_id")

    @web_application_id.setter
    def web_application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_application_id", value)


class ApplicationErrorRules(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_errors: Optional[pulumi.Input[Union['ApplicationErrorRulesCustomErrorsArgs', 'ApplicationErrorRulesCustomErrorsArgsDict']]] = None,
                 http_errors: Optional[pulumi.Input[Union['ApplicationErrorRulesHttpErrorsArgs', 'ApplicationErrorRulesHttpErrorsArgsDict']]] = None,
                 ignore_custom_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_http_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_js_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 web_application_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ApplicationErrorRules resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ApplicationErrorRulesCustomErrorsArgs', 'ApplicationErrorRulesCustomErrorsArgsDict']] custom_errors: (Field has overlap with `WebAppCustomErrors`) An ordered list of HTTP errors.
        :param pulumi.Input[Union['ApplicationErrorRulesHttpErrorsArgs', 'ApplicationErrorRulesHttpErrorsArgsDict']] http_errors: (Field has overlap with `WebAppRequestErrors`) An ordered list of HTTP errors. Rules are evaluated from top to bottom;
               the first matching rule applies
        :param pulumi.Input[bool] ignore_custom_errors_apdex: (Field has overlap with `WebAppCustomErrors`) Exclude (`true`) or include (`false`) custom errors listed in
               **customErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_http_errors_apdex: (Field has overlap with `WebAppRequestErrors`) Exclude (`true`) or include (`false`) HTTP errors listed in
               **httpErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_js_errors_apdex: Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation
        :param pulumi.Input[str] web_application_id: The EntityID of the the WebApplication
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ApplicationErrorRulesArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ApplicationErrorRules resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ApplicationErrorRulesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationErrorRulesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_errors: Optional[pulumi.Input[Union['ApplicationErrorRulesCustomErrorsArgs', 'ApplicationErrorRulesCustomErrorsArgsDict']]] = None,
                 http_errors: Optional[pulumi.Input[Union['ApplicationErrorRulesHttpErrorsArgs', 'ApplicationErrorRulesHttpErrorsArgsDict']]] = None,
                 ignore_custom_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_http_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 ignore_js_errors_apdex: Optional[pulumi.Input[bool]] = None,
                 web_application_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationErrorRulesArgs.__new__(ApplicationErrorRulesArgs)

            __props__.__dict__["custom_errors"] = custom_errors
            __props__.__dict__["http_errors"] = http_errors
            __props__.__dict__["ignore_custom_errors_apdex"] = ignore_custom_errors_apdex
            __props__.__dict__["ignore_http_errors_apdex"] = ignore_http_errors_apdex
            __props__.__dict__["ignore_js_errors_apdex"] = ignore_js_errors_apdex
            __props__.__dict__["web_application_id"] = web_application_id
        super(ApplicationErrorRules, __self__).__init__(
            'dynatrace:index/applicationErrorRules:ApplicationErrorRules',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_errors: Optional[pulumi.Input[Union['ApplicationErrorRulesCustomErrorsArgs', 'ApplicationErrorRulesCustomErrorsArgsDict']]] = None,
            http_errors: Optional[pulumi.Input[Union['ApplicationErrorRulesHttpErrorsArgs', 'ApplicationErrorRulesHttpErrorsArgsDict']]] = None,
            ignore_custom_errors_apdex: Optional[pulumi.Input[bool]] = None,
            ignore_http_errors_apdex: Optional[pulumi.Input[bool]] = None,
            ignore_js_errors_apdex: Optional[pulumi.Input[bool]] = None,
            web_application_id: Optional[pulumi.Input[str]] = None) -> 'ApplicationErrorRules':
        """
        Get an existing ApplicationErrorRules resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ApplicationErrorRulesCustomErrorsArgs', 'ApplicationErrorRulesCustomErrorsArgsDict']] custom_errors: (Field has overlap with `WebAppCustomErrors`) An ordered list of HTTP errors.
        :param pulumi.Input[Union['ApplicationErrorRulesHttpErrorsArgs', 'ApplicationErrorRulesHttpErrorsArgsDict']] http_errors: (Field has overlap with `WebAppRequestErrors`) An ordered list of HTTP errors. Rules are evaluated from top to bottom;
               the first matching rule applies
        :param pulumi.Input[bool] ignore_custom_errors_apdex: (Field has overlap with `WebAppCustomErrors`) Exclude (`true`) or include (`false`) custom errors listed in
               **customErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_http_errors_apdex: (Field has overlap with `WebAppRequestErrors`) Exclude (`true`) or include (`false`) HTTP errors listed in
               **httpErrorRules** in Apdex calculation
        :param pulumi.Input[bool] ignore_js_errors_apdex: Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation
        :param pulumi.Input[str] web_application_id: The EntityID of the the WebApplication
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApplicationErrorRulesState.__new__(_ApplicationErrorRulesState)

        __props__.__dict__["custom_errors"] = custom_errors
        __props__.__dict__["http_errors"] = http_errors
        __props__.__dict__["ignore_custom_errors_apdex"] = ignore_custom_errors_apdex
        __props__.__dict__["ignore_http_errors_apdex"] = ignore_http_errors_apdex
        __props__.__dict__["ignore_js_errors_apdex"] = ignore_js_errors_apdex
        __props__.__dict__["web_application_id"] = web_application_id
        return ApplicationErrorRules(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customErrors")
    def custom_errors(self) -> pulumi.Output[Optional['outputs.ApplicationErrorRulesCustomErrors']]:
        """
        (Field has overlap with `WebAppCustomErrors`) An ordered list of HTTP errors.
        """
        return pulumi.get(self, "custom_errors")

    @property
    @pulumi.getter(name="httpErrors")
    def http_errors(self) -> pulumi.Output[Optional['outputs.ApplicationErrorRulesHttpErrors']]:
        """
        (Field has overlap with `WebAppRequestErrors`) An ordered list of HTTP errors. Rules are evaluated from top to bottom;
        the first matching rule applies
        """
        return pulumi.get(self, "http_errors")

    @property
    @pulumi.getter(name="ignoreCustomErrorsApdex")
    def ignore_custom_errors_apdex(self) -> pulumi.Output[Optional[bool]]:
        """
        (Field has overlap with `WebAppCustomErrors`) Exclude (`true`) or include (`false`) custom errors listed in
        **customErrorRules** in Apdex calculation
        """
        return pulumi.get(self, "ignore_custom_errors_apdex")

    @property
    @pulumi.getter(name="ignoreHttpErrorsApdex")
    def ignore_http_errors_apdex(self) -> pulumi.Output[Optional[bool]]:
        """
        (Field has overlap with `WebAppRequestErrors`) Exclude (`true`) or include (`false`) HTTP errors listed in
        **httpErrorRules** in Apdex calculation
        """
        return pulumi.get(self, "ignore_http_errors_apdex")

    @property
    @pulumi.getter(name="ignoreJsErrorsApdex")
    def ignore_js_errors_apdex(self) -> pulumi.Output[Optional[bool]]:
        """
        Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation
        """
        return pulumi.get(self, "ignore_js_errors_apdex")

    @property
    @pulumi.getter(name="webApplicationId")
    def web_application_id(self) -> pulumi.Output[Optional[str]]:
        """
        The EntityID of the the WebApplication
        """
        return pulumi.get(self, "web_application_id")

