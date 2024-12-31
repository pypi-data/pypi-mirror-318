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

__all__ = ['CalculatedSyntheticMetricArgs', 'CalculatedSyntheticMetric']

@pulumi.input_type
class CalculatedSyntheticMetricArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 metric: pulumi.Input[str],
                 metric_key: pulumi.Input[str],
                 monitor_identifier: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]]] = None,
                 filter: Optional[pulumi.Input['CalculatedSyntheticMetricFilterArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CalculatedSyntheticMetric resource.
        :param pulumi.Input[bool] enabled: The metric is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[str] metric: The type of the synthetic metric. Possible values: [ ApplicationCache, Callback, CumulativeLayoutShift, DNSLookup, DOMComplete, DOMContentLoaded, DOMInteractive, FailedRequestsResources, FirstContentfulPaint, FirstInputDelay, FirstInputStart, FirstPaint, HTMLDownloaded, HttpErrors, JavaScriptErrors, LargestContentfulPaint, LoadEventEnd, LoadEventStart, LongTasks, NavigationStart, OnDOMContentLoaded, OnLoad, Processing, RedirectTime, Request, RequestStart, ResourceCount, Response, SecureConnect, SpeedIndex, TCPConnect, TimeToFirstByte, TotalDuration, TransferSize, UserActionDuration, VisuallyComplete ]
        :param pulumi.Input[str] metric_key: The unique key of the calculated synthetic metric.
        :param pulumi.Input[str] monitor_identifier: The Dynatrace entity ID of the monitor to which the metric belongs.
        :param pulumi.Input[str] description: Descriptor of a calculated synthetic metric.
        :param pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]] dimensions: Dimension of the calculated synthetic metric.
        :param pulumi.Input['CalculatedSyntheticMetricFilterArgs'] filter: Filter of the calculated synthetic metric.
        :param pulumi.Input[str] name: The displayed name of the metric.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "metric", metric)
        pulumi.set(__self__, "metric_key", metric_key)
        pulumi.set(__self__, "monitor_identifier", monitor_identifier)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        The metric is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def metric(self) -> pulumi.Input[str]:
        """
        The type of the synthetic metric. Possible values: [ ApplicationCache, Callback, CumulativeLayoutShift, DNSLookup, DOMComplete, DOMContentLoaded, DOMInteractive, FailedRequestsResources, FirstContentfulPaint, FirstInputDelay, FirstInputStart, FirstPaint, HTMLDownloaded, HttpErrors, JavaScriptErrors, LargestContentfulPaint, LoadEventEnd, LoadEventStart, LongTasks, NavigationStart, OnDOMContentLoaded, OnLoad, Processing, RedirectTime, Request, RequestStart, ResourceCount, Response, SecureConnect, SpeedIndex, TCPConnect, TimeToFirstByte, TotalDuration, TransferSize, UserActionDuration, VisuallyComplete ]
        """
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric", value)

    @property
    @pulumi.getter(name="metricKey")
    def metric_key(self) -> pulumi.Input[str]:
        """
        The unique key of the calculated synthetic metric.
        """
        return pulumi.get(self, "metric_key")

    @metric_key.setter
    def metric_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_key", value)

    @property
    @pulumi.getter(name="monitorIdentifier")
    def monitor_identifier(self) -> pulumi.Input[str]:
        """
        The Dynatrace entity ID of the monitor to which the metric belongs.
        """
        return pulumi.get(self, "monitor_identifier")

    @monitor_identifier.setter
    def monitor_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "monitor_identifier", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Descriptor of a calculated synthetic metric.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]]]:
        """
        Dimension of the calculated synthetic metric.
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['CalculatedSyntheticMetricFilterArgs']]:
        """
        Filter of the calculated synthetic metric.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['CalculatedSyntheticMetricFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The displayed name of the metric.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CalculatedSyntheticMetricState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filter: Optional[pulumi.Input['CalculatedSyntheticMetricFilterArgs']] = None,
                 metric: Optional[pulumi.Input[str]] = None,
                 metric_key: Optional[pulumi.Input[str]] = None,
                 monitor_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CalculatedSyntheticMetric resources.
        :param pulumi.Input[str] description: Descriptor of a calculated synthetic metric.
        :param pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]] dimensions: Dimension of the calculated synthetic metric.
        :param pulumi.Input[bool] enabled: The metric is enabled (`true`) or disabled (`false`)
        :param pulumi.Input['CalculatedSyntheticMetricFilterArgs'] filter: Filter of the calculated synthetic metric.
        :param pulumi.Input[str] metric: The type of the synthetic metric. Possible values: [ ApplicationCache, Callback, CumulativeLayoutShift, DNSLookup, DOMComplete, DOMContentLoaded, DOMInteractive, FailedRequestsResources, FirstContentfulPaint, FirstInputDelay, FirstInputStart, FirstPaint, HTMLDownloaded, HttpErrors, JavaScriptErrors, LargestContentfulPaint, LoadEventEnd, LoadEventStart, LongTasks, NavigationStart, OnDOMContentLoaded, OnLoad, Processing, RedirectTime, Request, RequestStart, ResourceCount, Response, SecureConnect, SpeedIndex, TCPConnect, TimeToFirstByte, TotalDuration, TransferSize, UserActionDuration, VisuallyComplete ]
        :param pulumi.Input[str] metric_key: The unique key of the calculated synthetic metric.
        :param pulumi.Input[str] monitor_identifier: The Dynatrace entity ID of the monitor to which the metric belongs.
        :param pulumi.Input[str] name: The displayed name of the metric.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if metric is not None:
            pulumi.set(__self__, "metric", metric)
        if metric_key is not None:
            pulumi.set(__self__, "metric_key", metric_key)
        if monitor_identifier is not None:
            pulumi.set(__self__, "monitor_identifier", monitor_identifier)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Descriptor of a calculated synthetic metric.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]]]:
        """
        Dimension of the calculated synthetic metric.
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CalculatedSyntheticMetricDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The metric is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['CalculatedSyntheticMetricFilterArgs']]:
        """
        Filter of the calculated synthetic metric.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['CalculatedSyntheticMetricFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the synthetic metric. Possible values: [ ApplicationCache, Callback, CumulativeLayoutShift, DNSLookup, DOMComplete, DOMContentLoaded, DOMInteractive, FailedRequestsResources, FirstContentfulPaint, FirstInputDelay, FirstInputStart, FirstPaint, HTMLDownloaded, HttpErrors, JavaScriptErrors, LargestContentfulPaint, LoadEventEnd, LoadEventStart, LongTasks, NavigationStart, OnDOMContentLoaded, OnLoad, Processing, RedirectTime, Request, RequestStart, ResourceCount, Response, SecureConnect, SpeedIndex, TCPConnect, TimeToFirstByte, TotalDuration, TransferSize, UserActionDuration, VisuallyComplete ]
        """
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric", value)

    @property
    @pulumi.getter(name="metricKey")
    def metric_key(self) -> Optional[pulumi.Input[str]]:
        """
        The unique key of the calculated synthetic metric.
        """
        return pulumi.get(self, "metric_key")

    @metric_key.setter
    def metric_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_key", value)

    @property
    @pulumi.getter(name="monitorIdentifier")
    def monitor_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The Dynatrace entity ID of the monitor to which the metric belongs.
        """
        return pulumi.get(self, "monitor_identifier")

    @monitor_identifier.setter
    def monitor_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monitor_identifier", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The displayed name of the metric.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class CalculatedSyntheticMetric(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CalculatedSyntheticMetricDimensionArgs', 'CalculatedSyntheticMetricDimensionArgsDict']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filter: Optional[pulumi.Input[Union['CalculatedSyntheticMetricFilterArgs', 'CalculatedSyntheticMetricFilterArgsDict']]] = None,
                 metric: Optional[pulumi.Input[str]] = None,
                 metric_key: Optional[pulumi.Input[str]] = None,
                 monitor_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CalculatedSyntheticMetric resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Descriptor of a calculated synthetic metric.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CalculatedSyntheticMetricDimensionArgs', 'CalculatedSyntheticMetricDimensionArgsDict']]]] dimensions: Dimension of the calculated synthetic metric.
        :param pulumi.Input[bool] enabled: The metric is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[Union['CalculatedSyntheticMetricFilterArgs', 'CalculatedSyntheticMetricFilterArgsDict']] filter: Filter of the calculated synthetic metric.
        :param pulumi.Input[str] metric: The type of the synthetic metric. Possible values: [ ApplicationCache, Callback, CumulativeLayoutShift, DNSLookup, DOMComplete, DOMContentLoaded, DOMInteractive, FailedRequestsResources, FirstContentfulPaint, FirstInputDelay, FirstInputStart, FirstPaint, HTMLDownloaded, HttpErrors, JavaScriptErrors, LargestContentfulPaint, LoadEventEnd, LoadEventStart, LongTasks, NavigationStart, OnDOMContentLoaded, OnLoad, Processing, RedirectTime, Request, RequestStart, ResourceCount, Response, SecureConnect, SpeedIndex, TCPConnect, TimeToFirstByte, TotalDuration, TransferSize, UserActionDuration, VisuallyComplete ]
        :param pulumi.Input[str] metric_key: The unique key of the calculated synthetic metric.
        :param pulumi.Input[str] monitor_identifier: The Dynatrace entity ID of the monitor to which the metric belongs.
        :param pulumi.Input[str] name: The displayed name of the metric.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CalculatedSyntheticMetricArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CalculatedSyntheticMetric resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CalculatedSyntheticMetricArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CalculatedSyntheticMetricArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CalculatedSyntheticMetricDimensionArgs', 'CalculatedSyntheticMetricDimensionArgsDict']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filter: Optional[pulumi.Input[Union['CalculatedSyntheticMetricFilterArgs', 'CalculatedSyntheticMetricFilterArgsDict']]] = None,
                 metric: Optional[pulumi.Input[str]] = None,
                 metric_key: Optional[pulumi.Input[str]] = None,
                 monitor_identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CalculatedSyntheticMetricArgs.__new__(CalculatedSyntheticMetricArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["dimensions"] = dimensions
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["filter"] = filter
            if metric is None and not opts.urn:
                raise TypeError("Missing required property 'metric'")
            __props__.__dict__["metric"] = metric
            if metric_key is None and not opts.urn:
                raise TypeError("Missing required property 'metric_key'")
            __props__.__dict__["metric_key"] = metric_key
            if monitor_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'monitor_identifier'")
            __props__.__dict__["monitor_identifier"] = monitor_identifier
            __props__.__dict__["name"] = name
        super(CalculatedSyntheticMetric, __self__).__init__(
            'dynatrace:index/calculatedSyntheticMetric:CalculatedSyntheticMetric',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CalculatedSyntheticMetricDimensionArgs', 'CalculatedSyntheticMetricDimensionArgsDict']]]]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            filter: Optional[pulumi.Input[Union['CalculatedSyntheticMetricFilterArgs', 'CalculatedSyntheticMetricFilterArgsDict']]] = None,
            metric: Optional[pulumi.Input[str]] = None,
            metric_key: Optional[pulumi.Input[str]] = None,
            monitor_identifier: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'CalculatedSyntheticMetric':
        """
        Get an existing CalculatedSyntheticMetric resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Descriptor of a calculated synthetic metric.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CalculatedSyntheticMetricDimensionArgs', 'CalculatedSyntheticMetricDimensionArgsDict']]]] dimensions: Dimension of the calculated synthetic metric.
        :param pulumi.Input[bool] enabled: The metric is enabled (`true`) or disabled (`false`)
        :param pulumi.Input[Union['CalculatedSyntheticMetricFilterArgs', 'CalculatedSyntheticMetricFilterArgsDict']] filter: Filter of the calculated synthetic metric.
        :param pulumi.Input[str] metric: The type of the synthetic metric. Possible values: [ ApplicationCache, Callback, CumulativeLayoutShift, DNSLookup, DOMComplete, DOMContentLoaded, DOMInteractive, FailedRequestsResources, FirstContentfulPaint, FirstInputDelay, FirstInputStart, FirstPaint, HTMLDownloaded, HttpErrors, JavaScriptErrors, LargestContentfulPaint, LoadEventEnd, LoadEventStart, LongTasks, NavigationStart, OnDOMContentLoaded, OnLoad, Processing, RedirectTime, Request, RequestStart, ResourceCount, Response, SecureConnect, SpeedIndex, TCPConnect, TimeToFirstByte, TotalDuration, TransferSize, UserActionDuration, VisuallyComplete ]
        :param pulumi.Input[str] metric_key: The unique key of the calculated synthetic metric.
        :param pulumi.Input[str] monitor_identifier: The Dynatrace entity ID of the monitor to which the metric belongs.
        :param pulumi.Input[str] name: The displayed name of the metric.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CalculatedSyntheticMetricState.__new__(_CalculatedSyntheticMetricState)

        __props__.__dict__["description"] = description
        __props__.__dict__["dimensions"] = dimensions
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["filter"] = filter
        __props__.__dict__["metric"] = metric
        __props__.__dict__["metric_key"] = metric_key
        __props__.__dict__["monitor_identifier"] = monitor_identifier
        __props__.__dict__["name"] = name
        return CalculatedSyntheticMetric(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Descriptor of a calculated synthetic metric.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Optional[Sequence['outputs.CalculatedSyntheticMetricDimension']]]:
        """
        Dimension of the calculated synthetic metric.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        The metric is enabled (`true`) or disabled (`false`)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional['outputs.CalculatedSyntheticMetricFilter']]:
        """
        Filter of the calculated synthetic metric.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def metric(self) -> pulumi.Output[str]:
        """
        The type of the synthetic metric. Possible values: [ ApplicationCache, Callback, CumulativeLayoutShift, DNSLookup, DOMComplete, DOMContentLoaded, DOMInteractive, FailedRequestsResources, FirstContentfulPaint, FirstInputDelay, FirstInputStart, FirstPaint, HTMLDownloaded, HttpErrors, JavaScriptErrors, LargestContentfulPaint, LoadEventEnd, LoadEventStart, LongTasks, NavigationStart, OnDOMContentLoaded, OnLoad, Processing, RedirectTime, Request, RequestStart, ResourceCount, Response, SecureConnect, SpeedIndex, TCPConnect, TimeToFirstByte, TotalDuration, TransferSize, UserActionDuration, VisuallyComplete ]
        """
        return pulumi.get(self, "metric")

    @property
    @pulumi.getter(name="metricKey")
    def metric_key(self) -> pulumi.Output[str]:
        """
        The unique key of the calculated synthetic metric.
        """
        return pulumi.get(self, "metric_key")

    @property
    @pulumi.getter(name="monitorIdentifier")
    def monitor_identifier(self) -> pulumi.Output[str]:
        """
        The Dynatrace entity ID of the monitor to which the metric belongs.
        """
        return pulumi.get(self, "monitor_identifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The displayed name of the metric.
        """
        return pulumi.get(self, "name")

