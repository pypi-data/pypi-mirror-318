"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.devtools.artifactregistry.v1beta2 import apt_artifact_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_apt__artifact__pb2
from .....google.devtools.artifactregistry.v1beta2 import file_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2
from .....google.devtools.artifactregistry.v1beta2 import package_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2
from .....google.devtools.artifactregistry.v1beta2 import repository_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2
from .....google.devtools.artifactregistry.v1beta2 import settings_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2
from .....google.devtools.artifactregistry.v1beta2 import tag_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2
from .....google.devtools.artifactregistry.v1beta2 import version_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2
from .....google.devtools.artifactregistry.v1beta2 import yum_artifact_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_yum__artifact__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/devtools/artifactregistry/v1beta2/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class ArtifactRegistryStub(object):
    """The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing artifacts
    from different package management systems.

    The resources managed by this API are:

    * Repositories, which group packages and their data.
    * Packages, which group versions and their tags.
    * Versions, which are specific forms of a package.
    * Tags, which represent alternative names for versions.
    * Files, which contain content and are optionally associated with a Package
    or Version.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ImportAptArtifacts = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ImportAptArtifacts', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_apt__artifact__pb2.ImportAptArtifactsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ImportYumArtifacts = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ImportYumArtifacts', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_yum__artifact__pb2.ImportYumArtifactsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListRepositories = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListRepositories', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.ListRepositoriesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.ListRepositoriesResponse.FromString, _registered_method=True)
        self.GetRepository = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.GetRepositoryRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.Repository.FromString, _registered_method=True)
        self.CreateRepository = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/CreateRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.CreateRepositoryRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateRepository = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/UpdateRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.UpdateRepositoryRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.Repository.FromString, _registered_method=True)
        self.DeleteRepository = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeleteRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.DeleteRepositoryRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListPackages = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListPackages', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.ListPackagesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.ListPackagesResponse.FromString, _registered_method=True)
        self.GetPackage = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetPackage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.GetPackageRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.Package.FromString, _registered_method=True)
        self.DeletePackage = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeletePackage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.DeletePackageRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListVersions = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListVersions', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.ListVersionsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.ListVersionsResponse.FromString, _registered_method=True)
        self.GetVersion = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetVersion', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.GetVersionRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.Version.FromString, _registered_method=True)
        self.DeleteVersion = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeleteVersion', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.DeleteVersionRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListFiles = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListFiles', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.ListFilesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.ListFilesResponse.FromString, _registered_method=True)
        self.GetFile = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetFile', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.GetFileRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.File.FromString, _registered_method=True)
        self.ListTags = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListTags', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.ListTagsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.ListTagsResponse.FromString, _registered_method=True)
        self.GetTag = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.GetTagRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.FromString, _registered_method=True)
        self.CreateTag = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/CreateTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.CreateTagRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.FromString, _registered_method=True)
        self.UpdateTag = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/UpdateTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.UpdateTagRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.FromString, _registered_method=True)
        self.DeleteTag = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeleteTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.DeleteTagRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.SetIamPolicy = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/SetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.GetIamPolicy = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.TestIamPermissions = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/TestIamPermissions', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, _registered_method=True)
        self.GetProjectSettings = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetProjectSettings', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.GetProjectSettingsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.ProjectSettings.FromString, _registered_method=True)
        self.UpdateProjectSettings = channel.unary_unary('/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/UpdateProjectSettings', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.UpdateProjectSettingsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.ProjectSettings.FromString, _registered_method=True)

class ArtifactRegistryServicer(object):
    """The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing artifacts
    from different package management systems.

    The resources managed by this API are:

    * Repositories, which group packages and their data.
    * Packages, which group versions and their tags.
    * Versions, which are specific forms of a package.
    * Tags, which represent alternative names for versions.
    * Files, which contain content and are optionally associated with a Package
    or Version.
    """

    def ImportAptArtifacts(self, request, context):
        """Imports Apt artifacts. The returned Operation will complete once the
        resources are imported. Package, Version, and File resources are created
        based on the imported artifacts. Imported artifacts that conflict with
        existing resources are ignored.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportYumArtifacts(self, request, context):
        """Imports Yum (RPM) artifacts. The returned Operation will complete once the
        resources are imported. Package, Version, and File resources are created
        based on the imported artifacts. Imported artifacts that conflict with
        existing resources are ignored.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRepositories(self, request, context):
        """Lists repositories.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRepository(self, request, context):
        """Gets a repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRepository(self, request, context):
        """Creates a repository. The returned Operation will finish once the
        repository has been created. Its response will be the created Repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRepository(self, request, context):
        """Updates a repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRepository(self, request, context):
        """Deletes a repository and all of its contents. The returned Operation will
        finish once the repository has been deleted. It will not have any Operation
        metadata and will return a google.protobuf.Empty response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPackages(self, request, context):
        """Lists packages.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPackage(self, request, context):
        """Gets a package.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePackage(self, request, context):
        """Deletes a package and all of its versions and tags. The returned operation
        will complete once the package has been deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVersions(self, request, context):
        """Lists versions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Gets a version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVersion(self, request, context):
        """Deletes a version and all of its content. The returned operation will
        complete once the version has been deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Lists files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """Gets a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTags(self, request, context):
        """Lists tags.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTag(self, request, context):
        """Gets a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTag(self, request, context):
        """Creates a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTag(self, request, context):
        """Updates a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTag(self, request, context):
        """Deletes a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetIamPolicy(self, request, context):
        """Updates the IAM policy for a given resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIamPolicy(self, request, context):
        """Gets the IAM policy for a given resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestIamPermissions(self, request, context):
        """Tests if the caller has a list of permissions on a resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProjectSettings(self, request, context):
        """Retrieves the Settings for the Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectSettings(self, request, context):
        """Updates the Settings for the Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ArtifactRegistryServicer_to_server(servicer, server):
    rpc_method_handlers = {'ImportAptArtifacts': grpc.unary_unary_rpc_method_handler(servicer.ImportAptArtifacts, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_apt__artifact__pb2.ImportAptArtifactsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ImportYumArtifacts': grpc.unary_unary_rpc_method_handler(servicer.ImportYumArtifacts, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_yum__artifact__pb2.ImportYumArtifactsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListRepositories': grpc.unary_unary_rpc_method_handler(servicer.ListRepositories, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.ListRepositoriesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.ListRepositoriesResponse.SerializeToString), 'GetRepository': grpc.unary_unary_rpc_method_handler(servicer.GetRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.GetRepositoryRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.Repository.SerializeToString), 'CreateRepository': grpc.unary_unary_rpc_method_handler(servicer.CreateRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.CreateRepositoryRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateRepository': grpc.unary_unary_rpc_method_handler(servicer.UpdateRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.UpdateRepositoryRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.Repository.SerializeToString), 'DeleteRepository': grpc.unary_unary_rpc_method_handler(servicer.DeleteRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.DeleteRepositoryRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListPackages': grpc.unary_unary_rpc_method_handler(servicer.ListPackages, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.ListPackagesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.ListPackagesResponse.SerializeToString), 'GetPackage': grpc.unary_unary_rpc_method_handler(servicer.GetPackage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.GetPackageRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.Package.SerializeToString), 'DeletePackage': grpc.unary_unary_rpc_method_handler(servicer.DeletePackage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.DeletePackageRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListVersions': grpc.unary_unary_rpc_method_handler(servicer.ListVersions, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.ListVersionsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.ListVersionsResponse.SerializeToString), 'GetVersion': grpc.unary_unary_rpc_method_handler(servicer.GetVersion, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.GetVersionRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.Version.SerializeToString), 'DeleteVersion': grpc.unary_unary_rpc_method_handler(servicer.DeleteVersion, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.DeleteVersionRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListFiles': grpc.unary_unary_rpc_method_handler(servicer.ListFiles, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.ListFilesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.ListFilesResponse.SerializeToString), 'GetFile': grpc.unary_unary_rpc_method_handler(servicer.GetFile, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.GetFileRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.File.SerializeToString), 'ListTags': grpc.unary_unary_rpc_method_handler(servicer.ListTags, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.ListTagsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.ListTagsResponse.SerializeToString), 'GetTag': grpc.unary_unary_rpc_method_handler(servicer.GetTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.GetTagRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.SerializeToString), 'CreateTag': grpc.unary_unary_rpc_method_handler(servicer.CreateTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.CreateTagRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.SerializeToString), 'UpdateTag': grpc.unary_unary_rpc_method_handler(servicer.UpdateTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.UpdateTagRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.SerializeToString), 'DeleteTag': grpc.unary_unary_rpc_method_handler(servicer.DeleteTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.DeleteTagRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'SetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.SetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'GetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.GetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'TestIamPermissions': grpc.unary_unary_rpc_method_handler(servicer.TestIamPermissions, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString), 'GetProjectSettings': grpc.unary_unary_rpc_method_handler(servicer.GetProjectSettings, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.GetProjectSettingsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.ProjectSettings.SerializeToString), 'UpdateProjectSettings': grpc.unary_unary_rpc_method_handler(servicer.UpdateProjectSettings, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.UpdateProjectSettingsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.ProjectSettings.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.devtools.artifactregistry.v1beta2.ArtifactRegistry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.devtools.artifactregistry.v1beta2.ArtifactRegistry', rpc_method_handlers)

class ArtifactRegistry(object):
    """The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing artifacts
    from different package management systems.

    The resources managed by this API are:

    * Repositories, which group packages and their data.
    * Packages, which group versions and their tags.
    * Versions, which are specific forms of a package.
    * Tags, which represent alternative names for versions.
    * Files, which contain content and are optionally associated with a Package
    or Version.
    """

    @staticmethod
    def ImportAptArtifacts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ImportAptArtifacts', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_apt__artifact__pb2.ImportAptArtifactsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ImportYumArtifacts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ImportYumArtifacts', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_yum__artifact__pb2.ImportYumArtifactsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListRepositories(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListRepositories', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.ListRepositoriesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.ListRepositoriesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetRepository', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.GetRepositoryRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.Repository.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/CreateRepository', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.CreateRepositoryRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/UpdateRepository', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.UpdateRepositoryRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.Repository.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeleteRepository', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_repository__pb2.DeleteRepositoryRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListPackages(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListPackages', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.ListPackagesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.ListPackagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetPackage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetPackage', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.GetPackageRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.Package.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeletePackage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeletePackage', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_package__pb2.DeletePackageRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListVersions', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.ListVersionsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.ListVersionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetVersion', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.GetVersionRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.Version.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeleteVersion', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_version__pb2.DeleteVersionRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListFiles(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListFiles', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.ListFilesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.ListFilesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetFile', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.GetFileRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_file__pb2.File.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTags(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/ListTags', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.ListTagsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.ListTagsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetTag', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.GetTagRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/CreateTag', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.CreateTagRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/UpdateTag', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.UpdateTagRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.Tag.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/DeleteTag', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_tag__pb2.DeleteTagRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/SetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def TestIamPermissions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/TestIamPermissions', google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetProjectSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/GetProjectSettings', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.GetProjectSettingsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.ProjectSettings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateProjectSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1beta2.ArtifactRegistry/UpdateProjectSettings', google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.UpdateProjectSettingsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1beta2_dot_settings__pb2.ProjectSettings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)