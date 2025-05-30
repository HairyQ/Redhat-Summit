# Step 2: ThingsBoard Deployment
ThingsBoard is an open-source platform for device management and telemetry streaming. This will be used to capture (via MQTT) and curate our telemetry data coming from virtual devices, and push it to OCI Streaming.

## ThingsBoard Delpoyment
The highlevel installation instructions are listed at the link below. Make sure to select the right deployment option for your need.

- https://thingsboard.io/docs/user-guide/install/installation-options/

## Openshift microservices deployment scripts

In order for the Thingsboard MQTT to work correctly, create a route for mqtt and modify the service **tb-mqtt-transport** and change the ServiceType from **ClusterIP** to **NodePort**. Modify the listener and use the Nodeport exposed by he service.

```yaml
kind: Route
apiVersion: route.openshift.io/v1
metadata:
  name: tb-route-mqtt-transport
  namespace: thingsboard
  annotations:
    openshift.io/host.generated: 'true'
spec:
  host: tb-route-mqtt-transport-thingsboard.apps.thingsboard.<USER-DOMAIN>
  path: /api/v1
  to:
    kind: Service
    name: tb-mqtt-transport
    weight: 100
  port:
    targetPort: mqtt
  tls:
    termination: edge
  wildcardPolicy: None
status:
  ingress:
    - host: tb-route-mqtt-transport-thingsboard.apps.thingsboard.<USER-DOMAIN>
      routerName: default
      conditions:
        - type: Admitted
          status: 'True'
      wildcardPolicy: None
      routerCanonicalHostname: apps.thingsboard.<USER-DOMAIN>
```
> Modify the **USER-DOMAIN** to your own domain


### Modify the Thingsboard Service to NodePort
Modify the thingsboard service from ClusterIP to NodePort

Source: https://github.com/thingsboard/thingsboard/issues/3637
  
