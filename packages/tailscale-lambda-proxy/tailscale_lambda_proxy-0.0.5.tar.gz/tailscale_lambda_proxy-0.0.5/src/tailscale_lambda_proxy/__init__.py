r'''
# replace this

WIP
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *

import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_lambda_nodejs as _aws_cdk_aws_lambda_nodejs_ceddda9d
import aws_cdk.aws_secretsmanager as _aws_cdk_aws_secretsmanager_ceddda9d
import constructs as _constructs_77d1e7e8
import tailscale_lambda_extension as _tailscale_lambda_extension_3efe799a


class TailscaleLambdaProxy(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="tailscale-lambda-proxy.TailscaleLambdaProxy",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ts_hostname: builtins.str,
        ts_secret_api_key: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
        options: typing.Optional[typing.Union["TailscaleLambdaProxyPropsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ts_hostname: The "Machine" name as shown in the Tailscale admin console that identifies the Lambda function.
        :param ts_secret_api_key: The name of the AWS Secrets Manager secret that contains the pure text Tailscale API Key.
        :param options: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__526fa7750b0e7b9422bb864d1636199d3eb6a8950c9fbe1a2634e109edb4970c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TailscaleLambdaProxyProps(
            ts_hostname=ts_hostname,
            ts_secret_api_key=ts_secret_api_key,
            options=options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(
        self,
    ) -> _tailscale_lambda_extension_3efe799a.TailscaleLambdaExtension:
        return typing.cast(_tailscale_lambda_extension_3efe799a.TailscaleLambdaExtension, jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> _aws_cdk_aws_lambda_nodejs_ceddda9d.NodejsFunction:
        return typing.cast(_aws_cdk_aws_lambda_nodejs_ceddda9d.NodejsFunction, jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFunctionUrl")
    def lambda_function_url(self) -> _aws_cdk_aws_lambda_ceddda9d.FunctionUrl:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.FunctionUrl, jsii.get(self, "lambdaFunctionUrl"))


@jsii.data_type(
    jsii_type="tailscale-lambda-proxy.TailscaleLambdaProxyProps",
    jsii_struct_bases=[],
    name_mapping={
        "ts_hostname": "tsHostname",
        "ts_secret_api_key": "tsSecretApiKey",
        "options": "options",
    },
)
class TailscaleLambdaProxyProps:
    def __init__(
        self,
        *,
        ts_hostname: builtins.str,
        ts_secret_api_key: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
        options: typing.Optional[typing.Union["TailscaleLambdaProxyPropsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ts_hostname: The "Machine" name as shown in the Tailscale admin console that identifies the Lambda function.
        :param ts_secret_api_key: The name of the AWS Secrets Manager secret that contains the pure text Tailscale API Key.
        :param options: 
        '''
        if isinstance(options, dict):
            options = TailscaleLambdaProxyPropsOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1db2d7dac4f0d91262bca503b92335b2c7da889dea02a4605b962b6c445b4e3)
            check_type(argname="argument ts_hostname", value=ts_hostname, expected_type=type_hints["ts_hostname"])
            check_type(argname="argument ts_secret_api_key", value=ts_secret_api_key, expected_type=type_hints["ts_secret_api_key"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ts_hostname": ts_hostname,
            "ts_secret_api_key": ts_secret_api_key,
        }
        if options is not None:
            self._values["options"] = options

    @builtins.property
    def ts_hostname(self) -> builtins.str:
        '''The "Machine" name as shown in the Tailscale admin console that identifies the Lambda function.'''
        result = self._values.get("ts_hostname")
        assert result is not None, "Required property 'ts_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ts_secret_api_key(self) -> _aws_cdk_aws_secretsmanager_ceddda9d.ISecret:
        '''The name of the AWS Secrets Manager secret that contains the pure text Tailscale API Key.'''
        result = self._values.get("ts_secret_api_key")
        assert result is not None, "Required property 'ts_secret_api_key' is missing"
        return typing.cast(_aws_cdk_aws_secretsmanager_ceddda9d.ISecret, result)

    @builtins.property
    def options(self) -> typing.Optional["TailscaleLambdaProxyPropsOptions"]:
        result = self._values.get("options")
        return typing.cast(typing.Optional["TailscaleLambdaProxyPropsOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TailscaleLambdaProxyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="tailscale-lambda-proxy.TailscaleLambdaProxyPropsLambdaOption",
    jsii_struct_bases=[],
    name_mapping={"function_name": "functionName"},
)
class TailscaleLambdaProxyPropsLambdaOption:
    def __init__(self, *, function_name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param function_name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbc605245a7905e261f1f575b026f71eb19dfac71fcdbbb59b18468ecce4a759)
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if function_name is not None:
            self._values["function_name"] = function_name

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TailscaleLambdaProxyPropsLambdaOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="tailscale-lambda-proxy.TailscaleLambdaProxyPropsOptions",
    jsii_struct_bases=[],
    name_mapping={"extension": "extension", "lambda_": "lambda"},
)
class TailscaleLambdaProxyPropsOptions:
    def __init__(
        self,
        *,
        extension: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.LayerVersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_: typing.Optional[typing.Union[TailscaleLambdaProxyPropsLambdaOption, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param extension: 
        :param lambda_: 
        '''
        if isinstance(extension, dict):
            extension = _aws_cdk_aws_lambda_ceddda9d.LayerVersionOptions(**extension)
        if isinstance(lambda_, dict):
            lambda_ = TailscaleLambdaProxyPropsLambdaOption(**lambda_)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f012a3e49f709451167b5aea4e5d5e6bec3630984d9d528d842997a018da94e7)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if extension is not None:
            self._values["extension"] = extension
        if lambda_ is not None:
            self._values["lambda_"] = lambda_

    @builtins.property
    def extension(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LayerVersionOptions]:
        result = self._values.get("extension")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LayerVersionOptions], result)

    @builtins.property
    def lambda_(self) -> typing.Optional[TailscaleLambdaProxyPropsLambdaOption]:
        result = self._values.get("lambda_")
        return typing.cast(typing.Optional[TailscaleLambdaProxyPropsLambdaOption], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TailscaleLambdaProxyPropsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "TailscaleLambdaProxy",
    "TailscaleLambdaProxyProps",
    "TailscaleLambdaProxyPropsLambdaOption",
    "TailscaleLambdaProxyPropsOptions",
]

publication.publish()

def _typecheckingstub__526fa7750b0e7b9422bb864d1636199d3eb6a8950c9fbe1a2634e109edb4970c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ts_hostname: builtins.str,
    ts_secret_api_key: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
    options: typing.Optional[typing.Union[TailscaleLambdaProxyPropsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1db2d7dac4f0d91262bca503b92335b2c7da889dea02a4605b962b6c445b4e3(
    *,
    ts_hostname: builtins.str,
    ts_secret_api_key: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
    options: typing.Optional[typing.Union[TailscaleLambdaProxyPropsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbc605245a7905e261f1f575b026f71eb19dfac71fcdbbb59b18468ecce4a759(
    *,
    function_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f012a3e49f709451167b5aea4e5d5e6bec3630984d9d528d842997a018da94e7(
    *,
    extension: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.LayerVersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_: typing.Optional[typing.Union[TailscaleLambdaProxyPropsLambdaOption, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
