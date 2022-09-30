from kserve import utils
from kserve import V1beta1InferenceService
from kserve import V1beta1InferenceServiceSpec
from kserve import V1beta1PredictorSpec
from kserve import V1beta1SKLearnSpec

namespace = utils.get_default_target_namespace()
name='sklearn-iris'
kserve_version='v1beta1'
api_version = constants.KSERVE_GROUP + '/' + kserve_version

isvc = V1beta1InferenceService(api_version=api_version,
                               kind=constants.KSERVE_KIND,
                               metadata=client.V1ObjectMeta(
                                   name=name, namespace=namespace, annotations={'sidecar.istio.io/inject':'false'}),
                               spec=V1beta1InferenceServiceSpec(
                               predictor=V1beta1PredictorSpec(
                               sklearn=(V1beta1SKLearnSpec(
                                   storage_uri="gs://kfserving-samples/models/sklearn/iris"))))
)
KServe = KServeClient()
KServe.create(isvc)
from kserve import utils
from kserve import V1beta1InferenceService
from kserve import V1beta1InferenceServiceSpec
from kserve import V1beta1PredictorSpec
from kserve import V1beta1SKLearnSpec

namespace = utils.get_default_target_namespace()
name='sklearn-iris'
kserve_version='v1beta1'
api_version = constants.KSERVE_GROUP + '/' + kserve_version

isvc = V1beta1InferenceService(api_version=api_version,
                               kind=constants.KSERVE_KIND,
                               metadata=client.V1ObjectMeta(
                                   name=name, namespace=namespace, annotations={'sidecar.istio.io/inject':'false'}),
                               spec=V1beta1InferenceServiceSpec(
                               predictor=V1beta1PredictorSpec(
                               sklearn=(V1beta1SKLearnSpec(
                                   storage_uri="gs://kfserving-samples/models/sklearn/iris"))))
)
KServe = KServeClient()
isvc_resp = KServe.get(name, namespace=namespace)
print(isvc_resp)
