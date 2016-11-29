from django.conf.urls import url
from VNF import views

urlpatterns = [
        url(r'^/nf_template/$', views.VNFTemplateAll.as_view(), name='VNF Template'),
        url(r'^/nf_template/(?P<vnf_id>[^/]+)/$', views.VNFTemplate.as_view(), name='VNF List'),
        url(r'^/nf_image/(?P<vnf_id>[^/]+)/$', views.VNFImage.as_view(), name='VNF image'),
        url(r'^/nffg/(?P<nf_fgraphs_id>[^/]+)/$', views.NFFGraphs.as_view(), name='NFFGraphs data'),
        url(r'^/nffg/$', views.NF_FGraphsAll.as_view(), name='nf_fgraphs list'),
        url(r'^/nffg_digest/$', views.NF_FGraphsAll_graphs_names.as_view(), name='nf_fgraphs list name'),
        url(r'^/nf_capability/(?P<capability>[^/]+)/$', views.Capability.as_view(), name='Capability')
]
