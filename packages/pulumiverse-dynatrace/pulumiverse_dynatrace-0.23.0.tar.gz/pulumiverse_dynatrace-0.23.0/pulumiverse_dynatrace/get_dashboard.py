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

__all__ = [
    'GetDashboardResult',
    'AwaitableGetDashboardResult',
    'get_dashboard',
    'get_dashboard_output',
]

@pulumi.output_type
class GetDashboardResult:
    """
    A collection of values returned by getDashboard.
    """
    def __init__(__self__, id=None, name=None, owner=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")


class AwaitableGetDashboardResult(GetDashboardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDashboardResult(
            id=self.id,
            name=self.name,
            owner=self.owner)


def get_dashboard(name: Optional[str] = None,
                  owner: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDashboardResult:
    """
    The `Dashboard` data source allows the dashboard ID to be retrieved by its name and owner.

    - `name` (String) - The name of the dashboard
    - `owner` (String) - The owner of the dashboard

    If multiple services match the given criteria, the first result will be retrieved.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_dynatrace as dynatrace

    example = dynatrace.get_dashboard(name="Terraform",
        owner="Hashicorp")
    pulumi.export("id", example.id)
    ```
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['owner'] = owner
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('dynatrace:index/getDashboard:getDashboard', __args__, opts=opts, typ=GetDashboardResult).value

    return AwaitableGetDashboardResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        owner=pulumi.get(__ret__, 'owner'))
def get_dashboard_output(name: Optional[pulumi.Input[str]] = None,
                         owner: Optional[pulumi.Input[str]] = None,
                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDashboardResult]:
    """
    The `Dashboard` data source allows the dashboard ID to be retrieved by its name and owner.

    - `name` (String) - The name of the dashboard
    - `owner` (String) - The owner of the dashboard

    If multiple services match the given criteria, the first result will be retrieved.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_dynatrace as dynatrace

    example = dynatrace.get_dashboard(name="Terraform",
        owner="Hashicorp")
    pulumi.export("id", example.id)
    ```
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['owner'] = owner
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('dynatrace:index/getDashboard:getDashboard', __args__, opts=opts, typ=GetDashboardResult)
    return __ret__.apply(lambda __response__: GetDashboardResult(
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        owner=pulumi.get(__response__, 'owner')))
