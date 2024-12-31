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

__all__ = ['DocumentArgs', 'Document']

@pulumi.input_type
class DocumentArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 type: pulumi.Input[str],
                 actor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 private: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Document resource.
        :param pulumi.Input[str] content: Document content as JSON
        :param pulumi.Input[str] type: Type of the document. Possible Values are `dashboard`, `launchpad` and `notebook`
        :param pulumi.Input[str] actor: The user context the executions of the document will happen with
        :param pulumi.Input[str] name: The name/name of the document
        :param pulumi.Input[str] owner: The ID of the owner of this document
        :param pulumi.Input[bool] private: Specifies whether the document is private or readable by everybody
        """
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "type", type)
        if actor is not None:
            pulumi.set(__self__, "actor", actor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if private is not None:
            pulumi.set(__self__, "private", private)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        Document content as JSON
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of the document. Possible Values are `dashboard`, `launchpad` and `notebook`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def actor(self) -> Optional[pulumi.Input[str]]:
        """
        The user context the executions of the document will happen with
        """
        return pulumi.get(self, "actor")

    @actor.setter
    def actor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name/name of the document
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the owner of this document
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def private(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the document is private or readable by everybody
        """
        return pulumi.get(self, "private")

    @private.setter
    def private(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "private", value)


@pulumi.input_type
class _DocumentState:
    def __init__(__self__, *,
                 actor: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 private: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Document resources.
        :param pulumi.Input[str] actor: The user context the executions of the document will happen with
        :param pulumi.Input[str] content: Document content as JSON
        :param pulumi.Input[str] name: The name/name of the document
        :param pulumi.Input[str] owner: The ID of the owner of this document
        :param pulumi.Input[bool] private: Specifies whether the document is private or readable by everybody
        :param pulumi.Input[str] type: Type of the document. Possible Values are `dashboard`, `launchpad` and `notebook`
        :param pulumi.Input[int] version: The version of the document
        """
        if actor is not None:
            pulumi.set(__self__, "actor", actor)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if private is not None:
            pulumi.set(__self__, "private", private)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def actor(self) -> Optional[pulumi.Input[str]]:
        """
        The user context the executions of the document will happen with
        """
        return pulumi.get(self, "actor")

    @actor.setter
    def actor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actor", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        Document content as JSON
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name/name of the document
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the owner of this document
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def private(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the document is private or readable by everybody
        """
        return pulumi.get(self, "private")

    @private.setter
    def private(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "private", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the document. Possible Values are `dashboard`, `launchpad` and `notebook`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        The version of the document
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class Document(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actor: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 private: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        > **Dynatrace SaaS only**

        > To utilize this resource, please define the environment variables `DT_CLIENT_ID`, `DT_CLIENT_SECRET`, `DT_ACCOUNT_ID` with an OAuth client including the following permissions: **Create and edit documents** (`document:documents:write`), **View documents** (`document:documents:read`) and **Delete documents** (`document:documents:delete`).

        > This resource is excluded by default in the export utility, please explicitly specify the resource to retrieve existing configuration.

        ## Dynatrace Documentation

        - Dynatrace Documents - https://########.apps.dynatrace.com/platform/swagger-ui/index.html?urls.primaryName=Document%20Service

        ## Resource Example Usage

        ```python
        import pulumi
        import json
        import pulumiverse_dynatrace as dynatrace

        this = dynatrace.Document("this",
            type="dashboard",
            content=json.dumps({
                "version": 13,
                "variables": [],
                "tiles": {
                    "0": {
                        "type": "markdown",
                        "title": "",
                        "content": "![Image of a Dashboard](https://dt-cdn.net/wp-content/uploads/2022/09/pic1____Dashboard-Preset___PNG.png)",
                    },
                    "1": {
                        "type": "data",
                        "title": "",
                        "query": "timeseries avg(dt.host.cpu.user)",
                        "queryConfig": {
                            "additionalFilters": {},
                            "version": "4.3.1",
                            "datatype": "metrics",
                            "metricKey": "dt.host.cpu.user",
                            "aggregation": "avg",
                            "by": [],
                        },
                        "subType": "dql-builder-metrics",
                        "visualization": "lineChart",
                        "visualizationSettings": {
                            "thresholds": [],
                            "chartSettings": {
                                "gapPolicy": "connect",
                                "circleChartSettings": {
                                    "groupingThresholdType": "relative",
                                    "groupingThresholdValue": 0,
                                    "valueType": "relative",
                                },
                                "categoryOverrides": {},
                                "fieldMapping": {
                                    "timestamp": "timeframe",
                                    "leftAxisValues": ["avg(dt.host.cpu.user)"],
                                    "leftAxisDimensions": [],
                                    "fields": [],
                                    "values": [],
                                },
                            },
                            "singleValue": {
                                "showLabel": True,
                                "label": "",
                                "prefixIcon": "",
                                "autoscale": True,
                                "alignment": "center",
                                "colorThresholdTarget": "value",
                            },
                            "table": {
                                "rowDensity": "condensed",
                                "enableSparklines": False,
                                "hiddenColumns": [],
                                "lineWrapIds": [],
                                "columnWidths": {},
                            },
                        },
                    },
                    "2": {
                        "type": "data",
                        "title": "",
                        "query": "timeseries avg(dt.host.memory.used)",
                        "queryConfig": {
                            "additionalFilters": {},
                            "version": "4.3.1",
                            "datatype": "metrics",
                            "metricKey": "dt.host.memory.used",
                            "aggregation": "avg",
                            "by": [],
                        },
                        "subType": "dql-builder-metrics",
                        "visualization": "lineChart",
                        "visualizationSettings": {
                            "thresholds": [],
                            "chartSettings": {
                                "gapPolicy": "connect",
                                "circleChartSettings": {
                                    "groupingThresholdType": "relative",
                                    "groupingThresholdValue": 0,
                                    "valueType": "relative",
                                },
                                "categoryOverrides": {},
                                "fieldMapping": {
                                    "timestamp": "timeframe",
                                    "leftAxisValues": ["avg(dt.host.memory.used)"],
                                    "leftAxisDimensions": [],
                                    "fields": [],
                                    "values": [],
                                },
                                "categoricalBarChartSettings": {},
                            },
                            "singleValue": {
                                "showLabel": True,
                                "label": "",
                                "prefixIcon": "",
                                "autoscale": True,
                                "alignment": "center",
                                "colorThresholdTarget": "value",
                            },
                            "table": {
                                "rowDensity": "condensed",
                                "enableSparklines": False,
                                "hiddenColumns": [],
                                "lineWrapIds": [],
                                "columnWidths": {},
                            },
                        },
                    },
                },
                "layouts": {
                    "0": {
                        "x": 0,
                        "y": 0,
                        "w": 24,
                        "h": 14,
                    },
                    "1": {
                        "x": 0,
                        "y": 14,
                        "w": 9,
                        "h": 6,
                    },
                    "2": {
                        "x": 15,
                        "y": 14,
                        "w": 9,
                        "h": 6,
                    },
                },
            }))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] actor: The user context the executions of the document will happen with
        :param pulumi.Input[str] content: Document content as JSON
        :param pulumi.Input[str] name: The name/name of the document
        :param pulumi.Input[str] owner: The ID of the owner of this document
        :param pulumi.Input[bool] private: Specifies whether the document is private or readable by everybody
        :param pulumi.Input[str] type: Type of the document. Possible Values are `dashboard`, `launchpad` and `notebook`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DocumentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **Dynatrace SaaS only**

        > To utilize this resource, please define the environment variables `DT_CLIENT_ID`, `DT_CLIENT_SECRET`, `DT_ACCOUNT_ID` with an OAuth client including the following permissions: **Create and edit documents** (`document:documents:write`), **View documents** (`document:documents:read`) and **Delete documents** (`document:documents:delete`).

        > This resource is excluded by default in the export utility, please explicitly specify the resource to retrieve existing configuration.

        ## Dynatrace Documentation

        - Dynatrace Documents - https://########.apps.dynatrace.com/platform/swagger-ui/index.html?urls.primaryName=Document%20Service

        ## Resource Example Usage

        ```python
        import pulumi
        import json
        import pulumiverse_dynatrace as dynatrace

        this = dynatrace.Document("this",
            type="dashboard",
            content=json.dumps({
                "version": 13,
                "variables": [],
                "tiles": {
                    "0": {
                        "type": "markdown",
                        "title": "",
                        "content": "![Image of a Dashboard](https://dt-cdn.net/wp-content/uploads/2022/09/pic1____Dashboard-Preset___PNG.png)",
                    },
                    "1": {
                        "type": "data",
                        "title": "",
                        "query": "timeseries avg(dt.host.cpu.user)",
                        "queryConfig": {
                            "additionalFilters": {},
                            "version": "4.3.1",
                            "datatype": "metrics",
                            "metricKey": "dt.host.cpu.user",
                            "aggregation": "avg",
                            "by": [],
                        },
                        "subType": "dql-builder-metrics",
                        "visualization": "lineChart",
                        "visualizationSettings": {
                            "thresholds": [],
                            "chartSettings": {
                                "gapPolicy": "connect",
                                "circleChartSettings": {
                                    "groupingThresholdType": "relative",
                                    "groupingThresholdValue": 0,
                                    "valueType": "relative",
                                },
                                "categoryOverrides": {},
                                "fieldMapping": {
                                    "timestamp": "timeframe",
                                    "leftAxisValues": ["avg(dt.host.cpu.user)"],
                                    "leftAxisDimensions": [],
                                    "fields": [],
                                    "values": [],
                                },
                            },
                            "singleValue": {
                                "showLabel": True,
                                "label": "",
                                "prefixIcon": "",
                                "autoscale": True,
                                "alignment": "center",
                                "colorThresholdTarget": "value",
                            },
                            "table": {
                                "rowDensity": "condensed",
                                "enableSparklines": False,
                                "hiddenColumns": [],
                                "lineWrapIds": [],
                                "columnWidths": {},
                            },
                        },
                    },
                    "2": {
                        "type": "data",
                        "title": "",
                        "query": "timeseries avg(dt.host.memory.used)",
                        "queryConfig": {
                            "additionalFilters": {},
                            "version": "4.3.1",
                            "datatype": "metrics",
                            "metricKey": "dt.host.memory.used",
                            "aggregation": "avg",
                            "by": [],
                        },
                        "subType": "dql-builder-metrics",
                        "visualization": "lineChart",
                        "visualizationSettings": {
                            "thresholds": [],
                            "chartSettings": {
                                "gapPolicy": "connect",
                                "circleChartSettings": {
                                    "groupingThresholdType": "relative",
                                    "groupingThresholdValue": 0,
                                    "valueType": "relative",
                                },
                                "categoryOverrides": {},
                                "fieldMapping": {
                                    "timestamp": "timeframe",
                                    "leftAxisValues": ["avg(dt.host.memory.used)"],
                                    "leftAxisDimensions": [],
                                    "fields": [],
                                    "values": [],
                                },
                                "categoricalBarChartSettings": {},
                            },
                            "singleValue": {
                                "showLabel": True,
                                "label": "",
                                "prefixIcon": "",
                                "autoscale": True,
                                "alignment": "center",
                                "colorThresholdTarget": "value",
                            },
                            "table": {
                                "rowDensity": "condensed",
                                "enableSparklines": False,
                                "hiddenColumns": [],
                                "lineWrapIds": [],
                                "columnWidths": {},
                            },
                        },
                    },
                },
                "layouts": {
                    "0": {
                        "x": 0,
                        "y": 0,
                        "w": 24,
                        "h": 14,
                    },
                    "1": {
                        "x": 0,
                        "y": 14,
                        "w": 9,
                        "h": 6,
                    },
                    "2": {
                        "x": 15,
                        "y": 14,
                        "w": 9,
                        "h": 6,
                    },
                },
            }))
        ```

        :param str resource_name: The name of the resource.
        :param DocumentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DocumentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actor: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 private: Optional[pulumi.Input[bool]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DocumentArgs.__new__(DocumentArgs)

            __props__.__dict__["actor"] = actor
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            __props__.__dict__["name"] = name
            __props__.__dict__["owner"] = owner
            __props__.__dict__["private"] = private
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["version"] = None
        super(Document, __self__).__init__(
            'dynatrace:index/document:Document',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actor: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            private: Optional[pulumi.Input[bool]] = None,
            type: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'Document':
        """
        Get an existing Document resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] actor: The user context the executions of the document will happen with
        :param pulumi.Input[str] content: Document content as JSON
        :param pulumi.Input[str] name: The name/name of the document
        :param pulumi.Input[str] owner: The ID of the owner of this document
        :param pulumi.Input[bool] private: Specifies whether the document is private or readable by everybody
        :param pulumi.Input[str] type: Type of the document. Possible Values are `dashboard`, `launchpad` and `notebook`
        :param pulumi.Input[int] version: The version of the document
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DocumentState.__new__(_DocumentState)

        __props__.__dict__["actor"] = actor
        __props__.__dict__["content"] = content
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        __props__.__dict__["private"] = private
        __props__.__dict__["type"] = type
        __props__.__dict__["version"] = version
        return Document(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actor(self) -> pulumi.Output[str]:
        """
        The user context the executions of the document will happen with
        """
        return pulumi.get(self, "actor")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        Document content as JSON
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name/name of the document
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        The ID of the owner of this document
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def private(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the document is private or readable by everybody
        """
        return pulumi.get(self, "private")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the document. Possible Values are `dashboard`, `launchpad` and `notebook`
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The version of the document
        """
        return pulumi.get(self, "version")

