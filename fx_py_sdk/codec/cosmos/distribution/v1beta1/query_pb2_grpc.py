# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fx_py_sdk.codec.cosmos.distribution.v1beta1 import query_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service for distribution module.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/Params',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
                )
        self.ValidatorOutstandingRewards = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/ValidatorOutstandingRewards',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorOutstandingRewardsRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorOutstandingRewardsResponse.FromString,
                )
        self.ValidatorCommission = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/ValidatorCommission',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorCommissionRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorCommissionResponse.FromString,
                )
        self.ValidatorSlashes = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/ValidatorSlashes',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorSlashesRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorSlashesResponse.FromString,
                )
        self.DelegationRewards = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/DelegationRewards',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationRewardsRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationRewardsResponse.FromString,
                )
        self.DelegationTotalRewards = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/DelegationTotalRewards',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationTotalRewardsRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationTotalRewardsResponse.FromString,
                )
        self.DelegatorValidators = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/DelegatorValidators',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.FromString,
                )
        self.DelegatorWithdrawAddress = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/DelegatorWithdrawAddress',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorWithdrawAddressRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorWithdrawAddressResponse.FromString,
                )
        self.CommunityPool = channel.unary_unary(
                '/cosmos.distribution.v1beta1.Query/CommunityPool',
                request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryCommunityPoolRequest.SerializeToString,
                response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryCommunityPoolResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service for distribution module.
    """

    def Params(self, request, context):
        """Params queries params of the distribution module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorOutstandingRewards(self, request, context):
        """ValidatorOutstandingRewards queries rewards of a validator address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorCommission(self, request, context):
        """ValidatorCommission queries accumulated commission for a validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorSlashes(self, request, context):
        """ValidatorSlashes queries slash events of a validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegationRewards(self, request, context):
        """DelegationRewards queries the total rewards accrued by a delegation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegationTotalRewards(self, request, context):
        """DelegationTotalRewards queries the total rewards accrued by a each
        validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorValidators(self, request, context):
        """DelegatorValidators queries the validators of a delegator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorWithdrawAddress(self, request, context):
        """DelegatorWithdrawAddress queries withdraw address of a delegator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommunityPool(self, request, context):
        """CommunityPool queries the community pool coins.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'ValidatorOutstandingRewards': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidatorOutstandingRewards,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorOutstandingRewardsRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorOutstandingRewardsResponse.SerializeToString,
            ),
            'ValidatorCommission': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidatorCommission,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorCommissionRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorCommissionResponse.SerializeToString,
            ),
            'ValidatorSlashes': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidatorSlashes,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorSlashesRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorSlashesResponse.SerializeToString,
            ),
            'DelegationRewards': grpc.unary_unary_rpc_method_handler(
                    servicer.DelegationRewards,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationRewardsRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationRewardsResponse.SerializeToString,
            ),
            'DelegationTotalRewards': grpc.unary_unary_rpc_method_handler(
                    servicer.DelegationTotalRewards,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationTotalRewardsRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationTotalRewardsResponse.SerializeToString,
            ),
            'DelegatorValidators': grpc.unary_unary_rpc_method_handler(
                    servicer.DelegatorValidators,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.SerializeToString,
            ),
            'DelegatorWithdrawAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.DelegatorWithdrawAddress,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorWithdrawAddressRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorWithdrawAddressResponse.SerializeToString,
            ),
            'CommunityPool': grpc.unary_unary_rpc_method_handler(
                    servicer.CommunityPool,
                    request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryCommunityPoolRequest.FromString,
                    response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryCommunityPoolResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.distribution.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service for distribution module.
    """

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/Params',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorOutstandingRewards(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/ValidatorOutstandingRewards',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorOutstandingRewardsRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorOutstandingRewardsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorCommission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/ValidatorCommission',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorCommissionRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorCommissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorSlashes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/ValidatorSlashes',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorSlashesRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryValidatorSlashesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegationRewards(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/DelegationRewards',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationRewardsRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationRewardsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegationTotalRewards(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/DelegationTotalRewards',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationTotalRewardsRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegationTotalRewardsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorValidators(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/DelegatorValidators',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorWithdrawAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/DelegatorWithdrawAddress',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorWithdrawAddressRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryDelegatorWithdrawAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommunityPool(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.distribution.v1beta1.Query/CommunityPool',
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryCommunityPoolRequest.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_query__pb2.QueryCommunityPoolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
