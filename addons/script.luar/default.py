# -*- coding: utf-8 -*-
#############################################################
#..Launcher version 1
#############################################################
import base64, codecs
elfary='q1nF5RnJSfo2pbXF5inltaEKWlo3V6VPptXlOuMTEiox5uoJHfVPqJMKWmnJ9hVPImVTEyVUO5qTuiovOholOwo21jLKEcLzkyWlNyVUO5K3MypaAco24cQDbtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPO4Lz1wM3IcYxEcLJkiMltcYz9eXPqSpaWipwbtWlNeVTSxMT9hGzSgMFjtp3ElXTHcXD0XVPNtVPNtVPOyrTy0XPxAPt0XVPNtVTI4L2IjqPOSrTAypUEco24tLKZtMGbAPvNtVPNtVPNtpREcLJkiMl5woT9mMFtcQDbtVPNtVPNtVUuvoJAaqJxhETyuoT9aXPxho2fbW0Ilpz9lBvNaVPftLJExo25BLJ1yYPOmqUVbMFxcQDbtVPNtVPNtVTI4nKDbXD0XQDbtVPNtMJkmMGbAPvNtVPNtVPNtq2y0nPOipTIhXTEyMzS1oUEspTS0nPjtW3qvWlxtLKZtMwbAPvNtVPNtVPNtVPNtVTLhq3WcqTHbMTS0LFxAPt0XVlO4Lz1wYzkiMluxMJMuqJk0K3OuqTtfVUuvoJZhGR9UFH5TGlxAPaORnJSfo2phqKOxLKEyXQRjZPxAPaORnJSfo2phL2kip2HbXD0XQDc4Lz1wM3IcYxEcLJkiMltcYz9eXTSxMT9hGzSgMFjtW0yhp3EuoTSwnJ9hVTMcozSfnKcuMTRhJ0AFKIyuVUO1MJEyplO2o2k2MKVtLFOyoaElLKVtpTSlLFOxnKAzpaI0LKVtMTHtMKA0MFOuMTEiov4aXD0XQDb='
judas='X3ZlcnNpb24NCnBEaWFsb2cudXBkYXRlKDIwKQ0KDQppZiBvcy5wYXRoLmV4aXN0cyhvcy5wYXRoLmpvaW4ocGF0aCxkZWZhdWx0X3ZlcnNpb24pKToNCiAgICBzaHV0aWwuY29weShvcy5wYXRoLmpvaW4ocGF0aCwgZGVmYXVsdF92ZXJzaW9uKSwgZGVmYXVsdF9wYXRoKQ0KDQplbHNlOg0KICAgICMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiAgICAjIHJlbW90bw0KICAgICMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiAgICB0cnk6DQogICAgICAgIHVybCA9ICdodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vY2lsaW5kcmEvbW90aC9tYXN0ZXIvc291cmNlLyVzLyVzJyAlIChhZGRvbnZlcnNpb24sIGRlZmF1bHRfdmVyc2lvbikNCiAgICAgICAgZGF0YSA9IHVybGxpYl9yZXF1ZXN0LnVybG9wZW4odXJsKS5yZWFkKCkNCg0KICAgIGV4Y2VwdCB1cmxsaWIuZXJyb3IuSFRUUEVycm9yIGFzIGU6DQogICAgICAgIHBEaWFsb2cuY2xvc2UoKQ0KICAgICAgICBpZiBlLmNvZGUgPT0gNDA0Og0KICAgICAgICAgICAgeGJtY2'
acdc='IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0NCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMuLkxhdW5jaGVyIHZlcnNpb24gMQ0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KDQppbXBvcnQgc3lzLCBvcywgcmUNCmltcG9ydCBzaHV0aWwNCmZyb20gc2l4Lm1vdmVzIGltcG9ydCB1cmxsaWJfcmVxdWVzdA0KZnJvbSBzaXgubW92ZXMgaW1wb3J0IHVybGxpYg0KaW1wb3J0IHNpeA0KaW1wb3J0IHhibWNndWksIHhibWNhZGRvbiwgeGJtYw0KDQp0cnk6DQogICAgaW1wb3J0IHhibWN2ZnMNCiAgICB0cmFuc2xhdGVQYXRoID0geGJtY3Zmcy50cmFuc2xhdGVQYXRoDQpleGNlcHQ6DQogICAgdHJhbnNsYXRlUGF0aCA9IHhibWMudHJhbnNsYXRlUGF0aA0KDQpydW50aW1lX3BhdGggPSB0cmFuc2xhdGVQYXRoKHhibWNhZGRvbi5BZGRvbigpLmdldEFkZG9uSW5mbygnUGF0aCcpKQ0KDQp3aXRoIG9wZW4ob3MucGF0aC5qb2luKHJ1bnRpbWVfcGF0aCwgJ2FkZG9uLnhtbCcpLCAncmInKSBhcyBmOg0KICAgIGFkZG9uID0gc2l4LmVuc3VyZV'
kiss='9mqUVbMv5lMJSxXPxcQDcuMTEioaMypaAco24tCFOlMF5znJ5xLJkfXUVaqzIlp2yioykmXw1pplbhXSkxX1jhKTDeKP5pMPfcWljtLJExo24cJmOqQDcuMTEiox5uoJHtCFO4Lz1wLJExo24hDJExo24bXF5aMKEOMTEioxyhMz8bW25uoJHaXFNeVPptWlNeVTSxMT9hqzIlp2yiot0XQDcjETyuoT9aVQ0trTWgL2q1nF5RnJSfo2qDpz9apzImpltcQDcjETyuoT9aYzAlMJS0MFuuMTEiox5uoJHfVPqDpzIjLKWuozEiVTyhp3EuoTSwnpBmov4hYvpcQDcjLKEbVQ0to3ZhpTS0nP5xnKWhLJ1yXT9mYaOuqTthLJWmpTS0nPusK2McoTIsKlxcQDcxMJMuqJk0K3OuqTttCFOipl5jLKEbYzcinJ4bpTS0nPjtW2EyMzS1oUDhpUxaXD0XQDcjrI92MKWmnJ9hVQ0tp3ElXUA5pl52MKWmnJ9hK2yhMz9oZS0cVPftWl4aVPftp3ElXUA5pl52MKWmnJ9hK2yhMz9oZI0cQDbAPvZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZAPvZtGR9QDHjAPvZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZAPzEyMzS1oUEsqzIlp2yiovN9VPqxMJMuqJk0KlImYaO5WlNyVUO5'
eval(compile(base64.b64decode(eval(base64.b64decode('ZXZhbCgnXHg2MVx4NjNceDY0XHg2MycpK2V2YWwoJ1x4NjNceDZmXHg2NFx4NjVceDYzXHg3M1x4MmVceDY0XHg2NVx4NjNceDZmXHg2NFx4NjVceDI4XHg2Ylx4NjlceDczXHg3M1x4MmNceDIwXHgyN1x4NzJceDZmXHg3NFx4MzFceDMzXHgyN1x4MjknKStldmFsKCdceDZhXHg3NVx4NjRceDYxXHg3MycpK2V2YWwoJ1x4NjNceDZmXHg2NFx4NjVceDYzXHg3M1x4MmVceDY0XHg2NVx4NjNceDZmXHg2NFx4NjVceDI4XHg2NVx4NmNceDY2XHg2MVx4NzJceDc5XHgyY1x4MjBceDI3XHg3Mlx4NmZceDc0XHgzMVx4MzNceDI3XHgyOScpCg=='))),'<string>','exec'))