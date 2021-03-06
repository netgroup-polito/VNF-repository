from django.conf.urls import url
from datastore import views

urlpatterns = [
        url(r'^/nf_template/$', views.VNFTemplateAll.as_view(), name='VNF Template'),
        url(r'^/nf_template/(?P<vnf_id>[^/]+)/$', views.VNFTemplate.as_view(), name='VNF List'),
        url(r'^/nf_image/chunked_upload/?$', views.MyChunkedUploadView.as_view(), name='api_chunked_upload'),
        url(r'^/nf_image/chunked_upload_complete/?$', views.MyChunkedUploadCompleteView.as_view(), name='api_chunked_upload_complete'),
        url(r'^/nf_image/(?P<vnf_id>[^/]+)/$', views.VNFImage.as_view(), name='VNF image'),
        url(r'^/nffg/(?P<nf_fgraph_id>[^/]+)/$', views.NFFGraphs.as_view(), name='NFFGraphs'),
        url(r'^/nffg/$', views.NFFGResource.as_view(), name='NFFGResource'),
        url(r'^/nffg_digest/$', views.nffg_digest.as_view(), name='nf_fgraphs list name'),
        url(r'^/nf_capability/(?P<capability>[^/]+)/$', views.Capability.as_view(), name='Capability')
]
