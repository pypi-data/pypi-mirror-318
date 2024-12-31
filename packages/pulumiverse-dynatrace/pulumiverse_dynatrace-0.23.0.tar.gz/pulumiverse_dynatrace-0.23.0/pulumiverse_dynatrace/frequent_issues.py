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

__all__ = ['FrequentIssuesArgs', 'FrequentIssues']

@pulumi.input_type
class FrequentIssuesArgs:
    def __init__(__self__, *,
                 detect_apps: pulumi.Input[bool],
                 detect_infra: pulumi.Input[bool],
                 detect_txn: pulumi.Input[bool],
                 detect_env: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a FrequentIssues resource.
        :param pulumi.Input[bool] detect_apps: Detect frequent issues within applications, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_infra: Detect frequent issues within infrastructure, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_txn: Detect frequent issues within transactions and services, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_env: Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.
        """
        pulumi.set(__self__, "detect_apps", detect_apps)
        pulumi.set(__self__, "detect_infra", detect_infra)
        pulumi.set(__self__, "detect_txn", detect_txn)
        if detect_env is not None:
            pulumi.set(__self__, "detect_env", detect_env)

    @property
    @pulumi.getter(name="detectApps")
    def detect_apps(self) -> pulumi.Input[bool]:
        """
        Detect frequent issues within applications, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_apps")

    @detect_apps.setter
    def detect_apps(self, value: pulumi.Input[bool]):
        pulumi.set(self, "detect_apps", value)

    @property
    @pulumi.getter(name="detectInfra")
    def detect_infra(self) -> pulumi.Input[bool]:
        """
        Detect frequent issues within infrastructure, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_infra")

    @detect_infra.setter
    def detect_infra(self, value: pulumi.Input[bool]):
        pulumi.set(self, "detect_infra", value)

    @property
    @pulumi.getter(name="detectTxn")
    def detect_txn(self) -> pulumi.Input[bool]:
        """
        Detect frequent issues within transactions and services, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_txn")

    @detect_txn.setter
    def detect_txn(self, value: pulumi.Input[bool]):
        pulumi.set(self, "detect_txn", value)

    @property
    @pulumi.getter(name="detectEnv")
    def detect_env(self) -> Optional[pulumi.Input[bool]]:
        """
        Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.
        """
        return pulumi.get(self, "detect_env")

    @detect_env.setter
    def detect_env(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detect_env", value)


@pulumi.input_type
class _FrequentIssuesState:
    def __init__(__self__, *,
                 detect_apps: Optional[pulumi.Input[bool]] = None,
                 detect_env: Optional[pulumi.Input[bool]] = None,
                 detect_infra: Optional[pulumi.Input[bool]] = None,
                 detect_txn: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering FrequentIssues resources.
        :param pulumi.Input[bool] detect_apps: Detect frequent issues within applications, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_env: Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.
        :param pulumi.Input[bool] detect_infra: Detect frequent issues within infrastructure, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_txn: Detect frequent issues within transactions and services, enabled (`true`) or disabled (`false`)
        """
        if detect_apps is not None:
            pulumi.set(__self__, "detect_apps", detect_apps)
        if detect_env is not None:
            pulumi.set(__self__, "detect_env", detect_env)
        if detect_infra is not None:
            pulumi.set(__self__, "detect_infra", detect_infra)
        if detect_txn is not None:
            pulumi.set(__self__, "detect_txn", detect_txn)

    @property
    @pulumi.getter(name="detectApps")
    def detect_apps(self) -> Optional[pulumi.Input[bool]]:
        """
        Detect frequent issues within applications, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_apps")

    @detect_apps.setter
    def detect_apps(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detect_apps", value)

    @property
    @pulumi.getter(name="detectEnv")
    def detect_env(self) -> Optional[pulumi.Input[bool]]:
        """
        Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.
        """
        return pulumi.get(self, "detect_env")

    @detect_env.setter
    def detect_env(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detect_env", value)

    @property
    @pulumi.getter(name="detectInfra")
    def detect_infra(self) -> Optional[pulumi.Input[bool]]:
        """
        Detect frequent issues within infrastructure, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_infra")

    @detect_infra.setter
    def detect_infra(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detect_infra", value)

    @property
    @pulumi.getter(name="detectTxn")
    def detect_txn(self) -> Optional[pulumi.Input[bool]]:
        """
        Detect frequent issues within transactions and services, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_txn")

    @detect_txn.setter
    def detect_txn(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detect_txn", value)


class FrequentIssues(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detect_apps: Optional[pulumi.Input[bool]] = None,
                 detect_env: Optional[pulumi.Input[bool]] = None,
                 detect_infra: Optional[pulumi.Input[bool]] = None,
                 detect_txn: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a FrequentIssues resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] detect_apps: Detect frequent issues within applications, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_env: Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.
        :param pulumi.Input[bool] detect_infra: Detect frequent issues within infrastructure, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_txn: Detect frequent issues within transactions and services, enabled (`true`) or disabled (`false`)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FrequentIssuesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a FrequentIssues resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param FrequentIssuesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FrequentIssuesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detect_apps: Optional[pulumi.Input[bool]] = None,
                 detect_env: Optional[pulumi.Input[bool]] = None,
                 detect_infra: Optional[pulumi.Input[bool]] = None,
                 detect_txn: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FrequentIssuesArgs.__new__(FrequentIssuesArgs)

            if detect_apps is None and not opts.urn:
                raise TypeError("Missing required property 'detect_apps'")
            __props__.__dict__["detect_apps"] = detect_apps
            __props__.__dict__["detect_env"] = detect_env
            if detect_infra is None and not opts.urn:
                raise TypeError("Missing required property 'detect_infra'")
            __props__.__dict__["detect_infra"] = detect_infra
            if detect_txn is None and not opts.urn:
                raise TypeError("Missing required property 'detect_txn'")
            __props__.__dict__["detect_txn"] = detect_txn
        super(FrequentIssues, __self__).__init__(
            'dynatrace:index/frequentIssues:FrequentIssues',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            detect_apps: Optional[pulumi.Input[bool]] = None,
            detect_env: Optional[pulumi.Input[bool]] = None,
            detect_infra: Optional[pulumi.Input[bool]] = None,
            detect_txn: Optional[pulumi.Input[bool]] = None) -> 'FrequentIssues':
        """
        Get an existing FrequentIssues resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] detect_apps: Detect frequent issues within applications, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_env: Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.
        :param pulumi.Input[bool] detect_infra: Detect frequent issues within infrastructure, enabled (`true`) or disabled (`false`)
        :param pulumi.Input[bool] detect_txn: Detect frequent issues within transactions and services, enabled (`true`) or disabled (`false`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FrequentIssuesState.__new__(_FrequentIssuesState)

        __props__.__dict__["detect_apps"] = detect_apps
        __props__.__dict__["detect_env"] = detect_env
        __props__.__dict__["detect_infra"] = detect_infra
        __props__.__dict__["detect_txn"] = detect_txn
        return FrequentIssues(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="detectApps")
    def detect_apps(self) -> pulumi.Output[bool]:
        """
        Detect frequent issues within applications, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_apps")

    @property
    @pulumi.getter(name="detectEnv")
    def detect_env(self) -> pulumi.Output[Optional[bool]]:
        """
        Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.
        """
        return pulumi.get(self, "detect_env")

    @property
    @pulumi.getter(name="detectInfra")
    def detect_infra(self) -> pulumi.Output[bool]:
        """
        Detect frequent issues within infrastructure, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_infra")

    @property
    @pulumi.getter(name="detectTxn")
    def detect_txn(self) -> pulumi.Output[bool]:
        """
        Detect frequent issues within transactions and services, enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "detect_txn")

