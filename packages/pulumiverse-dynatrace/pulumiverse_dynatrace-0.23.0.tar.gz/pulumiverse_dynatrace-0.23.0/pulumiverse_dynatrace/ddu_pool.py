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

__all__ = ['DduPoolArgs', 'DduPool']

@pulumi.input_type
class DduPoolArgs:
    def __init__(__self__, *,
                 events: Optional[pulumi.Input['DduPoolEventsArgs']] = None,
                 log_monitoring: Optional[pulumi.Input['DduPoolLogMonitoringArgs']] = None,
                 metrics: Optional[pulumi.Input['DduPoolMetricsArgs']] = None,
                 serverless: Optional[pulumi.Input['DduPoolServerlessArgs']] = None,
                 traces: Optional[pulumi.Input['DduPoolTracesArgs']] = None):
        """
        The set of arguments for constructing a DduPool resource.
        :param pulumi.Input['DduPoolEventsArgs'] events: DDU pool settings for Events
        :param pulumi.Input['DduPoolLogMonitoringArgs'] log_monitoring: DDU pool settings for Log Monitoring
        :param pulumi.Input['DduPoolMetricsArgs'] metrics: DDU pool settings for Metrics
        :param pulumi.Input['DduPoolServerlessArgs'] serverless: DDU pool settings for Serverless
        :param pulumi.Input['DduPoolTracesArgs'] traces: DDU pool settings for Traces
        """
        if events is not None:
            pulumi.set(__self__, "events", events)
        if log_monitoring is not None:
            pulumi.set(__self__, "log_monitoring", log_monitoring)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if serverless is not None:
            pulumi.set(__self__, "serverless", serverless)
        if traces is not None:
            pulumi.set(__self__, "traces", traces)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input['DduPoolEventsArgs']]:
        """
        DDU pool settings for Events
        """
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input['DduPoolEventsArgs']]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter(name="logMonitoring")
    def log_monitoring(self) -> Optional[pulumi.Input['DduPoolLogMonitoringArgs']]:
        """
        DDU pool settings for Log Monitoring
        """
        return pulumi.get(self, "log_monitoring")

    @log_monitoring.setter
    def log_monitoring(self, value: Optional[pulumi.Input['DduPoolLogMonitoringArgs']]):
        pulumi.set(self, "log_monitoring", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input['DduPoolMetricsArgs']]:
        """
        DDU pool settings for Metrics
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input['DduPoolMetricsArgs']]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter
    def serverless(self) -> Optional[pulumi.Input['DduPoolServerlessArgs']]:
        """
        DDU pool settings for Serverless
        """
        return pulumi.get(self, "serverless")

    @serverless.setter
    def serverless(self, value: Optional[pulumi.Input['DduPoolServerlessArgs']]):
        pulumi.set(self, "serverless", value)

    @property
    @pulumi.getter
    def traces(self) -> Optional[pulumi.Input['DduPoolTracesArgs']]:
        """
        DDU pool settings for Traces
        """
        return pulumi.get(self, "traces")

    @traces.setter
    def traces(self, value: Optional[pulumi.Input['DduPoolTracesArgs']]):
        pulumi.set(self, "traces", value)


@pulumi.input_type
class _DduPoolState:
    def __init__(__self__, *,
                 events: Optional[pulumi.Input['DduPoolEventsArgs']] = None,
                 log_monitoring: Optional[pulumi.Input['DduPoolLogMonitoringArgs']] = None,
                 metrics: Optional[pulumi.Input['DduPoolMetricsArgs']] = None,
                 serverless: Optional[pulumi.Input['DduPoolServerlessArgs']] = None,
                 traces: Optional[pulumi.Input['DduPoolTracesArgs']] = None):
        """
        Input properties used for looking up and filtering DduPool resources.
        :param pulumi.Input['DduPoolEventsArgs'] events: DDU pool settings for Events
        :param pulumi.Input['DduPoolLogMonitoringArgs'] log_monitoring: DDU pool settings for Log Monitoring
        :param pulumi.Input['DduPoolMetricsArgs'] metrics: DDU pool settings for Metrics
        :param pulumi.Input['DduPoolServerlessArgs'] serverless: DDU pool settings for Serverless
        :param pulumi.Input['DduPoolTracesArgs'] traces: DDU pool settings for Traces
        """
        if events is not None:
            pulumi.set(__self__, "events", events)
        if log_monitoring is not None:
            pulumi.set(__self__, "log_monitoring", log_monitoring)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if serverless is not None:
            pulumi.set(__self__, "serverless", serverless)
        if traces is not None:
            pulumi.set(__self__, "traces", traces)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input['DduPoolEventsArgs']]:
        """
        DDU pool settings for Events
        """
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input['DduPoolEventsArgs']]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter(name="logMonitoring")
    def log_monitoring(self) -> Optional[pulumi.Input['DduPoolLogMonitoringArgs']]:
        """
        DDU pool settings for Log Monitoring
        """
        return pulumi.get(self, "log_monitoring")

    @log_monitoring.setter
    def log_monitoring(self, value: Optional[pulumi.Input['DduPoolLogMonitoringArgs']]):
        pulumi.set(self, "log_monitoring", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input['DduPoolMetricsArgs']]:
        """
        DDU pool settings for Metrics
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input['DduPoolMetricsArgs']]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter
    def serverless(self) -> Optional[pulumi.Input['DduPoolServerlessArgs']]:
        """
        DDU pool settings for Serverless
        """
        return pulumi.get(self, "serverless")

    @serverless.setter
    def serverless(self, value: Optional[pulumi.Input['DduPoolServerlessArgs']]):
        pulumi.set(self, "serverless", value)

    @property
    @pulumi.getter
    def traces(self) -> Optional[pulumi.Input['DduPoolTracesArgs']]:
        """
        DDU pool settings for Traces
        """
        return pulumi.get(self, "traces")

    @traces.setter
    def traces(self, value: Optional[pulumi.Input['DduPoolTracesArgs']]):
        pulumi.set(self, "traces", value)


class DduPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 events: Optional[pulumi.Input[Union['DduPoolEventsArgs', 'DduPoolEventsArgsDict']]] = None,
                 log_monitoring: Optional[pulumi.Input[Union['DduPoolLogMonitoringArgs', 'DduPoolLogMonitoringArgsDict']]] = None,
                 metrics: Optional[pulumi.Input[Union['DduPoolMetricsArgs', 'DduPoolMetricsArgsDict']]] = None,
                 serverless: Optional[pulumi.Input[Union['DduPoolServerlessArgs', 'DduPoolServerlessArgsDict']]] = None,
                 traces: Optional[pulumi.Input[Union['DduPoolTracesArgs', 'DduPoolTracesArgsDict']]] = None,
                 __props__=None):
        """
        !> This resource API endpoint has been deprecated.

        > This resource requires the API token scopes **Read settings** (`settings.read`) and **Write settings** (`settings.write`)

        ## Dynatrace Documentation

        - DDU Pools - https://www.dynatrace.com/support/help/monitoring-consumption/davis-data-units#ddu-pools

        - Settings API - https://www.dynatrace.com/support/help/dynatrace-api/environment-api/settings (schemaId: `builtin:accounting.ddu.limit`)

        ## Resource Example Usage

        ```python
        import pulumi
        import pulumiverse_dynatrace as dynatrace

        _name_ = dynatrace.DduPool("#name#",
            events={
                "enabled": True,
                "type": "MONTHLY",
                "value": 125,
            },
            log_monitoring={
                "enabled": True,
                "type": "MONTHLY",
                "value": 124,
            },
            metrics={
                "enabled": True,
                "type": "MONTHLY",
                "value": 123,
            },
            serverless={
                "enabled": True,
                "type": "MONTHLY",
                "value": 126,
            },
            traces={
                "enabled": True,
                "type": "MONTHLY",
                "value": 127,
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DduPoolEventsArgs', 'DduPoolEventsArgsDict']] events: DDU pool settings for Events
        :param pulumi.Input[Union['DduPoolLogMonitoringArgs', 'DduPoolLogMonitoringArgsDict']] log_monitoring: DDU pool settings for Log Monitoring
        :param pulumi.Input[Union['DduPoolMetricsArgs', 'DduPoolMetricsArgsDict']] metrics: DDU pool settings for Metrics
        :param pulumi.Input[Union['DduPoolServerlessArgs', 'DduPoolServerlessArgsDict']] serverless: DDU pool settings for Serverless
        :param pulumi.Input[Union['DduPoolTracesArgs', 'DduPoolTracesArgsDict']] traces: DDU pool settings for Traces
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DduPoolArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        !> This resource API endpoint has been deprecated.

        > This resource requires the API token scopes **Read settings** (`settings.read`) and **Write settings** (`settings.write`)

        ## Dynatrace Documentation

        - DDU Pools - https://www.dynatrace.com/support/help/monitoring-consumption/davis-data-units#ddu-pools

        - Settings API - https://www.dynatrace.com/support/help/dynatrace-api/environment-api/settings (schemaId: `builtin:accounting.ddu.limit`)

        ## Resource Example Usage

        ```python
        import pulumi
        import pulumiverse_dynatrace as dynatrace

        _name_ = dynatrace.DduPool("#name#",
            events={
                "enabled": True,
                "type": "MONTHLY",
                "value": 125,
            },
            log_monitoring={
                "enabled": True,
                "type": "MONTHLY",
                "value": 124,
            },
            metrics={
                "enabled": True,
                "type": "MONTHLY",
                "value": 123,
            },
            serverless={
                "enabled": True,
                "type": "MONTHLY",
                "value": 126,
            },
            traces={
                "enabled": True,
                "type": "MONTHLY",
                "value": 127,
            })
        ```

        :param str resource_name: The name of the resource.
        :param DduPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DduPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 events: Optional[pulumi.Input[Union['DduPoolEventsArgs', 'DduPoolEventsArgsDict']]] = None,
                 log_monitoring: Optional[pulumi.Input[Union['DduPoolLogMonitoringArgs', 'DduPoolLogMonitoringArgsDict']]] = None,
                 metrics: Optional[pulumi.Input[Union['DduPoolMetricsArgs', 'DduPoolMetricsArgsDict']]] = None,
                 serverless: Optional[pulumi.Input[Union['DduPoolServerlessArgs', 'DduPoolServerlessArgsDict']]] = None,
                 traces: Optional[pulumi.Input[Union['DduPoolTracesArgs', 'DduPoolTracesArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DduPoolArgs.__new__(DduPoolArgs)

            __props__.__dict__["events"] = events
            __props__.__dict__["log_monitoring"] = log_monitoring
            __props__.__dict__["metrics"] = metrics
            __props__.__dict__["serverless"] = serverless
            __props__.__dict__["traces"] = traces
        super(DduPool, __self__).__init__(
            'dynatrace:index/dduPool:DduPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            events: Optional[pulumi.Input[Union['DduPoolEventsArgs', 'DduPoolEventsArgsDict']]] = None,
            log_monitoring: Optional[pulumi.Input[Union['DduPoolLogMonitoringArgs', 'DduPoolLogMonitoringArgsDict']]] = None,
            metrics: Optional[pulumi.Input[Union['DduPoolMetricsArgs', 'DduPoolMetricsArgsDict']]] = None,
            serverless: Optional[pulumi.Input[Union['DduPoolServerlessArgs', 'DduPoolServerlessArgsDict']]] = None,
            traces: Optional[pulumi.Input[Union['DduPoolTracesArgs', 'DduPoolTracesArgsDict']]] = None) -> 'DduPool':
        """
        Get an existing DduPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DduPoolEventsArgs', 'DduPoolEventsArgsDict']] events: DDU pool settings for Events
        :param pulumi.Input[Union['DduPoolLogMonitoringArgs', 'DduPoolLogMonitoringArgsDict']] log_monitoring: DDU pool settings for Log Monitoring
        :param pulumi.Input[Union['DduPoolMetricsArgs', 'DduPoolMetricsArgsDict']] metrics: DDU pool settings for Metrics
        :param pulumi.Input[Union['DduPoolServerlessArgs', 'DduPoolServerlessArgsDict']] serverless: DDU pool settings for Serverless
        :param pulumi.Input[Union['DduPoolTracesArgs', 'DduPoolTracesArgsDict']] traces: DDU pool settings for Traces
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DduPoolState.__new__(_DduPoolState)

        __props__.__dict__["events"] = events
        __props__.__dict__["log_monitoring"] = log_monitoring
        __props__.__dict__["metrics"] = metrics
        __props__.__dict__["serverless"] = serverless
        __props__.__dict__["traces"] = traces
        return DduPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Optional['outputs.DduPoolEvents']]:
        """
        DDU pool settings for Events
        """
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="logMonitoring")
    def log_monitoring(self) -> pulumi.Output[Optional['outputs.DduPoolLogMonitoring']]:
        """
        DDU pool settings for Log Monitoring
        """
        return pulumi.get(self, "log_monitoring")

    @property
    @pulumi.getter
    def metrics(self) -> pulumi.Output[Optional['outputs.DduPoolMetrics']]:
        """
        DDU pool settings for Metrics
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def serverless(self) -> pulumi.Output[Optional['outputs.DduPoolServerless']]:
        """
        DDU pool settings for Serverless
        """
        return pulumi.get(self, "serverless")

    @property
    @pulumi.getter
    def traces(self) -> pulumi.Output[Optional['outputs.DduPoolTraces']]:
        """
        DDU pool settings for Traces
        """
        return pulumi.get(self, "traces")

