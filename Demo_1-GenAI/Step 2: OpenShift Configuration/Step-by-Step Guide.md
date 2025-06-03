# Step 2: OpenShift Configuration
This step will demonstrate how to create an OpenShift cluster and add GPU nodes to the cluster. This cluster will be supporting our NVIDIA NIM nodes and additional worker nodes.
## 1. Create OpenShift Account

### 1.1. Create a account on Red Hat Portal
- https://console.redhat.com/openshift

## 2. Create OpenShift Cluster

OCI is certified to use OpenShift versions starting 4.14.

### 2.1 Follow the instructions below to provision an OpenShift Cluster
- https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/installing_on_oci/installing-oci-assisted-installer
- https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/overview.htm

#### 2.1.1 The highlevel deployment Workflow using Assisted Installer is:

The procedure for using the Assisted Installer in a connected environment to install a cluster on OCI is outlined below:

1. In the OCI console, configure an OCI account to host the cluster:

    i. Create a new child compartment under an existing compartment.
   
    ii. Create a new object storage bucket or use one provided by OCI.

    iii. Download the stack file template stored locally.

3. In the Assisted Installer console, set up a cluster:

    i. Enter the cluster configurations.
    
    ii. Generate and download the discovery ISO image.

3. In the OCI console, create the infrastructure:

    i. Upload the discovery ISO image to the OCI bucket.
   
    ii. Create a Pre-Authenticated Request (PAR) for the ISO image.

    iii. Upload the stack file template, and use it to create and apply the stack.

    iv. Copy the custom manifest YAML file from the stack.\

    NOTE: If deploying NVIDIA NIMs for Gen AI workloads, you may want to consider a GPU shape to support the compute.

5. In the Assisted Installer console, complete the cluster installation:

    i. Set roles for the cluster nodes.
   
    ii. Upload the manifests provided by Oracle.
   
    iii. Install the cluster.

## Links
[oci-openshift Resource Manager Template](https://github.com/oracle-quickstart/oci-openshift)
[OCI Certified Shapes for OpenShift](https://catalog.redhat.com/cloud/detail/216977)

...
