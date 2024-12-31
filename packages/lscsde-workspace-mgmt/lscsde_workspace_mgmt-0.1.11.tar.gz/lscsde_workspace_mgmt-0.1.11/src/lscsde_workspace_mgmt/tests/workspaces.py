from pydantic import TypeAdapter

from ..objects import (
    AnalyticsWorkspace,
    AnalyticsWorkspaceConverter
)

class TestWorkspace:
    def test_workspace_conversion(self):
        workspace_dict = self.mock_workspace()
        print(workspace_dict)
        adaptor = TypeAdapter(AnalyticsWorkspace)
        workspace = adaptor.validate_python(workspace_dict, strict=False)
        assert "example-jupyter-workspace" == workspace.metadata.name 
        assert "jupyter/datascience-notebook:latest" == workspace.spec.jupyter_workspace.image
        assert "2024-02-26" == workspace.spec.validity.available_from
        assert "2124-02-26" == workspace.spec.validity.expires
        assert "Example jupyter workspace" == workspace.spec.display_name
        assert "This is an example jupyter workspace, and can be largely ignored\n" == workspace.spec.description

    def test_workspace_conversion_to_dict(self):
        adaptor = TypeAdapter(AnalyticsWorkspace)
        workspace_dict = self.mock_workspace()
        workspace = adaptor.validate_python(workspace_dict)
        workspace_converted = adaptor.dump_python(workspace, by_alias=True)
        print(workspace_converted)
        assert "xlscsde.nhs.uk/v1" == workspace_converted["apiVersion"]
        assert "AnalyticsWorkspace" == workspace_converted["kind"]
        assert "example-jupyter-workspace" == workspace_converted["metadata"]["name"]
        assert "jupyter/datascience-notebook:latest" == workspace_converted["spec"]["jupyterWorkspace"]["image"]
        assert "2024-02-26" == workspace_converted["spec"]["validity"]["availableFrom"]
        assert "2124-02-26" == workspace_converted["spec"]["validity"]["expires"]
        assert "Example jupyter workspace" == workspace_converted["spec"]["displayName"]
        assert "This is an example jupyter workspace, and can be largely ignored\n" == workspace_converted["spec"]["description"]

    def test_workspace_conversion_to_workspace_dict(self):
        adaptor = TypeAdapter(AnalyticsWorkspace)
        workspace_dict = self.mock_workspace()
        workspace = adaptor.validate_python(workspace_dict)
        converter = AnalyticsWorkspaceConverter()
        ws = converter.to_workspace_dict(workspace=workspace)
        assert ws["display_name"] == "Example jupyter workspace"
        assert ws["description"] == "This is an example jupyter workspace, and can be largely ignored\n"
        assert ws["kubespawner_override"] != None
        assert ws["kubespawner_override"]["image"] == "jupyter/datascience-notebook:latest"
        assert ws["kubespawner_override"]["extra_labels"] != None
        assert ws["kubespawner_override"]["extra_labels"]["workspace"] == "example-jupyter-workspace"
        assert ws["slug"] == "example-jupyter-workspace"
        assert ws["start_date"] == "2024-02-26"
        assert ws["end_date"] == "2124-02-26"

    def mock_workspace(self):
        return {
            'apiVersion': 'xlscsde.nhs.uk/v1', 
            'kind': 'AnalyticsWorkspace', 
            'metadata': {
                'annotations': {
                    'meta.helm.sh/release-name': 'xlscsde-ws-mgmt', 
                    'meta.helm.sh/release-namespace': 'default'
                }, 
                'creationTimestamp': '2024-02-27T10:37:58Z', 
                'generation': 1, 
                'labels': {
                    'app.kubernetes.io/managed-by': 'Helm'
                }, 
                'managedFields': [
                    {
                        'apiVersion': 'xlscsde.nhs.uk/v1', 
                        'fieldsType': 'FieldsV1', 
                        'fieldsV1': {'f:metadata': {'f:annotations': {'.': {}, 'f:meta.helm.sh/release-name': {}, 'f:meta.helm.sh/release-namespace': {}}, 'f:labels': {'.': {}, 'f:app.kubernetes.io/managed-by': {}}}, 'f:spec': {'.': {}, 'f:description': {}, 'f:displayName': {}, 'f:jupyterWorkspace': {'.': {}, 'f:image': {}}, 'f:validity': {'.': {}, 'f:availableFrom': {}, 'f:expires': {}}}}, 
                        'manager': 'helm', 
                        'operation': 'Update', 
                        'time': '2024-02-27T10:37:58Z'
                    }
                ], 
                'name': 'example-jupyter-workspace', 
                'namespace': 'default', 
                'resourceVersion': '834601', 
                'uid': '190997a8-3bf6-4a9f-8302-4db6018c8a93'
            }, 
            'spec': {
                'description': 'This is an example jupyter workspace, and can be largely ignored\n', 
                'displayName': 'Example jupyter workspace', 
                'jupyterWorkspace': {
                    'image': 'jupyter/datascience-notebook:latest'
                }, 
                'validity': {
                    'availableFrom': '2024-02-26', 
                    'expires': '2124-02-26'
                }
            }
        }