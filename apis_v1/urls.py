# apis_v1/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-
"""
This is called from config/urls.py like this:
    url(r'^apis/v1/', include('apis_v1.urls', namespace="apis_v1")),
"""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from apis_v1.views import views_docs, views_ballot, views_candidate, views_donation, views_facebook, views_friend, \
    views_misc, views_organization, views_position, views_twitter, views_voter
from ballot.views_admin import ballot_items_sync_out_view, ballot_returned_sync_out_view
from candidate.views_admin import candidates_sync_out_view
from election.views_admin import elections_sync_out_view
from issue.views_admin import issues_sync_out_view
from measure.views_admin import measures_sync_out_view
from office.views_admin import offices_sync_out_view
from organization.views_admin import organizations_sync_out_view
from polling_location.views_admin import polling_locations_sync_out_view
from position.views_admin import positions_sync_out_view
from voter_guide.views_admin import voter_guides_sync_out_view


urlpatterns = [
    # Actual API Calls
    url(r'^ballotItemOptionsRetrieve/', views_ballot.ballot_item_options_retrieve_view,
        name='ballotItemOptionsRetrieveView'),
    url(r'^ballotItemRetrieve/', views_ballot.ballot_item_retrieve_view, name='ballotItemRetrieveView'),
    url(r'^ballotItemsSyncOut/', ballot_items_sync_out_view, name='ballotItemsSyncOutView'),
    url(r'^ballotReturnedSyncOut/', ballot_returned_sync_out_view, name='ballotReturnedSyncOutView'),
    url(r'^candidateRetrieve/', views_candidate.candidate_retrieve_view, name='candidateRetrieveView'),
    url(r'^candidatesRetrieve/', views_candidate.candidates_retrieve_view, name='candidatesRetrieveView'),
    url(r'^candidatesSyncOut/', candidates_sync_out_view, name='candidatesSyncOutView'),
    url(r'^deviceIdGenerate/$', views_misc.device_id_generate_view, name='deviceIdGenerateView'),
    url(r'^donationWithStripe', views_donation.donation_with_stripe_view, name='donationWithStripeView'),
    url(r'^donationStripeWebhook/', views_donation.donation_stripe_webhook_view, name='donationStripeWebhookView'),
    url(r'^electionsSyncOut/', elections_sync_out_view, name='electionsSyncOutView'),
    url(r'^facebookDisconnect/', views_facebook.facebook_disconnect_view, name='facebookDisconnectView'),
    url(r'^facebookFriendsAction/', views_facebook.facebook_friends_action_view, name='facebookFriendsActionView'),
    url(r'^friendInvitationByEmailSend/',
        views_friend.friend_invitation_by_email_send_view, name='friendInvitationByEmailSendView'),
    url(r'^friendInvitationByEmailVerify/',
        views_friend.friend_invitation_by_email_verify_view, name='friendInvitationByEmailVerifyView'),
    url(r'^friendInvitationByFacebookSend/',
        views_friend.friend_invitation_by_facebook_send_view, name='friendInvitationByFacebookSendView'),
    url(r'^friendInvitationByFacebookVerify/',
        views_friend.friend_invitation_by_facebook_verify_view, name='friendInvitationByFacebookVerifyView'),
    url(r'^friendInvitationByWeVoteIdSend/',
        views_friend.friend_invitation_by_we_vote_id_send_view, name='friendInvitationByWeVoteIdSendView'),
    url(r'^friendInviteResponse/', views_friend.friend_invite_response_view, name='friendInviteResponseView'),
    url(r'^friendList/', views_friend.friend_list_view, name='friendListView'),
    url(r'^issuesSyncOut/', issues_sync_out_view, name='issuesSyncOutView'),
    url(r'^measureRetrieve/', views_misc.measure_retrieve_view, name='measureRetrieveView'),
    url(r'^measuresSyncOut/', measures_sync_out_view, name='measuresSyncOutView'),
    url(r'^officeRetrieve/', views_misc.office_retrieve_view, name='officeRetrieveView'),
    url(r'^officesSyncOut/', offices_sync_out_view, name='officesSyncOutView'),
    url(r'^organizationCount/', views_organization.organization_count_view, name='organizationCountView'),
    url(r'^organizationFollow/', views_organization.organization_follow_api_view, name='organizationFollowView'),
    url(r'^organizationFollowIgnore/', views_organization.organization_follow_ignore_api_view,
        name='organizationFollowIgnoreView'),
    url(r'^organizationRetrieve/', views_organization.organization_retrieve_view, name='organizationRetrieveView'),
    url(r'^organizationSave/', views_organization.organization_save_view, name='organizationSaveView'),
    url(r'^organizationSearch/', views_organization.organization_search_view, name='organizationSearchView'),
    url(r'^organizationsSyncOut/', organizations_sync_out_view, name='organizationsSyncOutView'),
    url(r'^organizationStopFollowing/',
        views_organization.organization_stop_following_api_view, name='organizationStopFollowingView'),
    url(r'^organizationsFollowedRetrieve/',
        views_organization.organizations_followed_retrieve_api_view, name='organizationsFollowedRetrieveView'),
    url(r'^organizationSuggestionTasks/',
        views_organization.organization_suggestion_tasks_view, name='organizationSuggestionTasksView'),
    url(r'^pollingLocationsSyncOut/', polling_locations_sync_out_view, name='pollingLocationsSyncOutView'),
    url(r'^positionsCountForAllBallotItems/',
        views_position.positions_count_for_all_ballot_items_view, name='positionsCountForAllBallotItemsView'),
    url(r'^positionsCountForOneBallotItem/',
        views_position.positions_count_for_one_ballot_item_view, name='positionsCountForOneBallotItemView'),
    url(r'^positionLikeCount/', views_position.position_like_count_view, name='positionLikeCountView'),
    url(r'^positionListForBallotItem/', views_position.position_list_for_ballot_item_view,
        name='positionListForBallotItemView'),
    url(r'^positionListForOpinionMaker/',
        views_position.position_list_for_opinion_maker_view, name='positionListForOpinionMakerView'),
    url(r'^positionListForVoter/',
        views_position.position_list_for_voter_view, name='positionListForVoterView'),
    url(r'^positionOpposeCountForBallotItem/',
        views_position.position_oppose_count_for_ballot_item_view, name='positionOpposeCountForBallotItemView'),
    url(r'^positionPublicOpposeCountForBallotItem/',
        views_position.position_public_oppose_count_for_ballot_item_view,
        name='positionPublicOpposeCountForBallotItemView'),
    url(r'^positionPublicSupportCountForBallotItem/',
        views_position.position_public_support_count_for_ballot_item_view,
        name='positionPublicSupportCountForBallotItemView'),
    url(r'^positionRetrieve/', views_position.position_retrieve_view, name='positionRetrieveView'),
    url(r'^positionSave/', views_position.position_save_view, name='positionSaveView'),
    url(r'^positionsSyncOut/', positions_sync_out_view, name='positionsSyncOutView'),
    url(r'^positionSupportCountForBallotItem/',
        views_position.position_support_count_for_ballot_item_view, name='positionSupportCountForBallotItemView'),
    url(r'^quickInfoRetrieve/', views_misc.quick_info_retrieve_view, name='quickInfoRetrieveView'),
    url(r'^searchAll/', views_misc.search_all_view, name='searchAllView'),
    url(r'^twitterIdentityRetrieve/', views_twitter.twitter_identity_retrieve_view, name='twitterIdentityRetrieveView'),
    url(r'^twitterSignInRequestAccessToken/',
        views_twitter.twitter_sign_in_request_access_token_view, name='twitterSignInRequestAccessTokenView'),
    url(r'^twitterSignInRequestVoterInfo/',
        views_twitter.twitter_sign_in_request_voter_info_view, name='twitterSignInRequestVoterInfoView'),
    url(r'^twitterSignInStart/', views_twitter.twitter_sign_in_start_view, name='twitterSignInStartView'),
    url(r'^twitterSignInRetrieve/', views_twitter.twitter_sign_in_retrieve_view, name='twitterSignInRetrieveView'),
    url (r'^twitterRetrieveIdsIFollow/',
         views_twitter.twitter_retrieve_ids_i_follow_view, name='twitterRetrieveIdsIFollowView'),
    url(r'^voterAddressRetrieve/', views_voter.voter_address_retrieve_view, name='voterAddressRetrieveView'),
    url(r'^voterAddressSave/', views_voter.voter_address_save_view, name='voterAddressSaveView'),
    url(r'^voterAllPositionsRetrieve/', views_voter.voter_all_positions_retrieve_view,
        name='voterAllPositionsRetrieveView'),
    url(r'^voterAllBookmarksStatusRetrieve/',
        views_voter.voter_all_bookmarks_status_retrieve_view, name='voterAllBookmarksStatusRetrieveView'),
    url(r'^voterBallotItemsRetrieve/', views_voter.voter_ballot_items_retrieve_view,
        name='voterBallotItemsRetrieveView'),
    url(r'^voterBallotItemsRetrieveFromGoogleCivic/',
        views_voter.voter_ballot_items_retrieve_from_google_civic_view,
        name='voterBallotItemsRetrieveFromGoogleCivicView'),
    url(r'^voterBallotListRetrieve/', views_voter.voter_ballot_list_retrieve_view, name='voterBallotListRetrieveView'),
    url(r'^voterBookmarkOffSave/', views_voter.voter_bookmark_off_save_view, name='voterBookmarkOffSaveView'),
    url(r'^voterBookmarkOnSave/', views_voter.voter_bookmark_on_save_view, name='voterBookmarkOnSaveView'),
    url(r'^voterBookmarkStatusRetrieve/', views_voter.voter_bookmark_status_retrieve_view,
        name='voterBookmarkStatusRetrieveView'),
    url(r'^voterCount/', views_voter.voter_count_view, name='voterCountView'),
    url(r'^voterCreate/', views_voter.voter_create_view, name='voterCreateView'),
    url(r'^voterEmailAddressRetrieve/', views_voter.voter_email_address_retrieve_view,
        name='voterEmailAddressRetrieveView'),
    url(r'^voterEmailAddressSave/', views_voter.voter_email_address_save_view, name='voterEmailAddressSaveView'),
    url(r'^voterEmailAddressSignIn/', views_voter.voter_email_address_sign_in_view, name='voterEmailAddressSignInView'),
    url(r'^voterEmailAddressVerify/', views_voter.voter_email_address_verify_view, name='voterEmailAddressVerifyView'),
    url(r'^voterExport/', views_voter.VoterExportView.as_view(), name='voterExportView'),
    url(r'^voterFacebookSaveToCurrentAccount/',
        views_facebook.voter_facebook_save_to_current_account_view, name='voterFacebookSaveToCurrentAccountView'),
    url(r'^voterFacebookSignInRetrieve/',
        views_voter.voter_facebook_sign_in_retrieve_view, name='voterFacebookSignInRetrieveView'),
    url(r'^voterFacebookSignInSave/',
        views_voter.voter_facebook_sign_in_save_view, name='voterFacebookSignInSaveView'),
    url(r'^voterGuidePossibilityRetrieve/',
        views_voter.voter_guide_possibility_retrieve_view, name='voterGuidePossibilityRetrieveView'),
    url(r'^voterGuidePossibilitySave/', views_voter.voter_guide_possibility_save_view,
        name='voterGuidePossibilitySaveView'),
    url(r'^voterGuidesFollowedRetrieve/',
        views_voter.voter_guides_followed_retrieve_view, name='voterGuidesFollowedRetrieveView'),
    url(r'^voterGuidesFollowedByOrganizationRetrieve/',
        views_voter.voter_guide_followed_by_organization_retrieve_view,
        name='voterGuidesFollowedByOrganizationRetrieveView'),
    url(r'^voterGuidesIgnoredRetrieve/',
        views_voter.voter_guides_ignored_retrieve_view, name='voterGuidesIgnoredRetrieveView'),
    url(r'^voterGuidesSyncOut/', voter_guides_sync_out_view, name='voterGuidesSyncOutView'),
    url(r'^voterGuidesToFollowRetrieve/',
        views_voter.voter_guides_to_follow_retrieve_view, name='voterGuidesToFollowRetrieveView'),
    url(r'^voterLocationRetrieveFromIP/',
        views_voter.voter_location_retrieve_from_ip_view, name='voterLocationRetrieveFromIPView'),
    url(r'^voterMergeTwoAccounts/', views_voter.voter_merge_two_accounts_view, name='voterMergeTwoAccountsView'),
    url(r'^voterOpposingSave/', views_voter.voter_opposing_save_view, name='voterOpposingSaveView'),
    url(r'^voterPhotoSave/', views_voter.voter_photo_save_view, name='voterPhotoSaveView'),
    url(r'^voterPositionCommentSave/', views_voter.voter_position_comment_save_view,
        name='voterPositionCommentSaveView'),
    url(r'^voterPositionLikeOffSave/', views_voter.voter_position_like_off_save_view,
        name='voterPositionLikeOffSaveView'),
    url(r'^voterPositionLikeOnSave/', views_voter.voter_position_like_on_save_view,
        name='voterPositionLikeOnSaveView'),
    url(r'^voterPositionLikeStatusRetrieve/',
        views_voter.voter_position_like_status_retrieve_view, name='voterPositionLikeStatusRetrieveView'),
    url(r'^voterPositionRetrieve/', views_voter.voter_position_retrieve_view, name='voterPositionRetrieveView'),
    url(r'^voterPositionVisibilitySave/',
        views_voter.voter_position_visibility_save_view, name='voterPositionVisibilitySaveView'),
    url(r'^voterRetrieve/', views_voter.voter_retrieve_view, name='voterRetrieveView'),
    url(r'^voterSignOut/', views_voter.voter_sign_out_view, name='voterSignOutView'),
    url(r'^voterSplitIntoTwoAccounts/', views_voter.voter_split_into_two_accounts_view, name='voterSplitIntoTwoAccountsView'),
    url(r'^voterStopOpposingSave/', views_voter.voter_stop_opposing_save_view, name='voterStopOpposingSaveView'),
    url(r'^voterStopSupportingSave/', views_voter.voter_stop_supporting_save_view, name='voterStopSupportingSaveView'),
    url(r'^voterSupportingSave/', views_voter.voter_supporting_save_view, name='voterSupportingSaveView'),
    url(r'^voterTwitterSaveToCurrentAccount/',
        views_voter.voter_twitter_save_to_current_account_view, name='voterTwitterSaveToCurrentAccountView'),
    url(r'^voterUpdate/', views_voter.voter_update_view, name='voterUpdateView'),

    ##########################
    # API Documentation Views
    url(r'^docs/$', views_docs.apis_index_doc_view, name='apisIndex'),
    url(r'^docs/ballotItemOptionsRetrieve/$',
        views_docs.ballot_item_options_retrieve_doc_view, name='ballotItemOptionsRetrieveDocs'),
    url(r'^docs/ballotItemRetrieve/$', views_docs.ballot_item_retrieve_doc_view, name='ballotItemRetrieveDocs'),
    url(r'^docs/ballotItemsSyncOut/$', views_docs.ballot_items_sync_out_doc_view, name='ballotItemsSyncOutDocs'),
    url(r'^docs/ballotReturnedSyncOut/$',
        views_docs.ballot_returned_sync_out_doc_view, name='ballotReturnedSyncOutDocs'),
    url(r'^docs/candidateRetrieve/$', views_docs.candidate_retrieve_doc_view, name='candidateRetrieveDocs'),
    url(r'^docs/candidatesRetrieve/$', views_docs.candidates_retrieve_doc_view, name='candidatesRetrieveDocs'),
    url(r'^docs/candidatesSyncOut/$', views_docs.candidates_sync_out_doc_view, name='candidatesSyncOutDocs'),
    url(r'^docs/deviceIdGenerate/$', views_docs.device_id_generate_doc_view, name='deviceIdGenerateDocs'),
    url(r'^docs/donationWithStripe/$', views_docs.donation_with_stripe_doc_view, name='donationWithStripeDocs'),
    url(r'^docs/electionsSyncOut/$', views_docs.elections_sync_out_doc_view, name='electionsSyncOutDocs'),
    url(r'^docs/facebookDisconnect/$', views_docs.facebook_disconnect_doc_view, name='facebookDisconnectDocs'),
    url(r'^docs/facebookFriendsAction/$',
        views_docs.facebook_friends_action_doc_view, name='facebookFriendsActionDocs'),
    url(r'^docs/friendInvitationByEmailSend/$',
        views_docs.friend_invitation_by_email_send_doc_view, name='friendInvitationByEmailSendDocs'),
    url(r'^docs/friendInvitationByEmailVerify/$',
        views_docs.friend_invitation_by_email_verify_doc_view, name='friendInvitationByEmailVerifyDocs'),
    url(r'^docs/friendInvitationByFacebookSend/$',
        views_docs.friend_invitation_by_facebook_send_doc_view, name='friendInvitationByFacebookSendDocs'),
    url(r'^docs/friendInvitationByFacebookVerify/$',
        views_docs.friend_invitation_by_facebook_verify_doc_view, name='friendInvitationByFacebookVerifyDocs'),
    url(r'^docs/friendInvitationByWeVoteIdSend/$',
        views_docs.friend_invitation_by_we_vote_id_send_doc_view, name='friendInvitationByWeVoteIdSendDocs'),
    url(r'^docs/friendInviteResponse/$', views_docs.friend_invite_response_doc_view, name='friendInviteResponseDocs'),
    url(r'^docs/friendList/$', views_docs.friend_list_doc_view, name='friendListDocs'),
    url(r'^docs/issuesSyncOut/$', views_docs.issues_sync_out_doc_view, name='issuesSyncOutDocs'),
    url(r'^docs/measureRetrieve/$', views_docs.measure_retrieve_doc_view, name='measureRetrieveDocs'),
    url(r'^docs/measuresSyncOut/$', views_docs.measures_sync_out_doc_view, name='measuresSyncOutDocs'),
    url(r'^docs/officeRetrieve/$', views_docs.office_retrieve_doc_view, name='officeRetrieveDocs'),
    url(r'^docs/officeSyncOut/$', views_docs.offices_sync_out_doc_view, name='officesSyncOutDocs'),
    url(r'^docs/organizationCount/$', views_docs.organization_count_doc_view, name='organizationCountDocs'),
    url(r'^docs/organizationFollow/', views_docs.organization_follow_doc_view, name='organizationFollowDocs'),
    url(r'^docs/organizationFollowIgnore/',
        views_docs.organization_follow_ignore_doc_view, name='organizationFollowIgnoreDocs'),
    url(r'^docs/organizationRetrieve/$', views_docs.organization_retrieve_doc_view, name='organizationRetrieveDocs'),
    url(r'^docs/organizationSave/$', views_docs.organization_save_doc_view, name='organizationSaveDocs'),
    url(r'^docs/organizationSearch/$', views_docs.organization_search_doc_view, name='organizationSearchDocs'),
    url(r'^docs/organizationsSyncOut/$', views_docs.organizations_sync_out_doc_view, name='organizationsSyncOutDocs'),
    url(r'^docs/organizationStopFollowing/',
        views_docs.organization_stop_following_doc_view, name='organizationStopFollowingDocs'),
    url(r'^docs/organizationsFollowedRetrieve/',
        views_docs.organizations_followed_retrieve_doc_view, name='organizationsFollowedRetrieveDocs'),
    url(r'^docs/organizationSuggestionTasks/',
        views_docs.organization_suggestion_tasks_doc_view, name='organizationSuggestionTasksDocs'),
    url(r'^docs/pollingLocationsSyncOut/$',
        views_docs.polling_locations_sync_out_doc_view, name='pollingLocationsSyncOutDocs'),
    url(r'^docs/positionLikeCount/$', views_docs.position_like_count_doc_view, name='positionLikeCountDocs'),
    url(r'^docs/positionListForBallotItem/',
        views_docs.position_list_for_ballot_item_doc_view, name='positionListForBallotItemDocs'),
    url(r'^docs/positionListForOpinionMaker/',
        views_docs.position_list_for_opinion_maker_doc_view, name='positionListForOpinionMakerDocs'),
    url(r'^docs/positionListForVoter/',
        views_docs.position_list_for_voter_doc_view, name='positionListForVoterDocs'),
    url(r'^docs/positionOpposeCountForBallotItem/',
        views_docs.position_oppose_count_for_ballot_item_doc_view, name='positionOpposeCountForBallotItemDocs'),
    url(r'^docs/positionPublicOpposeCountForBallotItem/',
        views_docs.position_public_oppose_count_for_ballot_item_doc_view,
        name='positionPublicOpposeCountForBallotItemDocs'),
    url(r'^docs/positionPublicSupportCountForBallotItem/',
        views_docs.position_public_support_count_for_ballot_item_doc_view,
        name='positionPublicSupportCountForBallotItemDocs'),
    url(r'^docs/positionRetrieve/$', views_docs.position_retrieve_doc_view, name='positionRetrieveDocs'),
    url(r'^docs/positionSave/$', views_docs.position_save_doc_view, name='positionSaveDocs'),
    url(r'^docs/positionsCountForAllBallotItemsDocs/$',
        views_docs.positions_count_for_all_ballot_items_doc_view, name='positionsCountForAllBallotItemsDocs'),
    url(r'^docs/positionsCountForOneBallotItemDocs/$',
        views_docs.positions_count_for_one_ballot_item_doc_view, name='positionsCountForOneBallotItemDocs'),
    url(r'^docs/positionsSyncOut/$', views_docs.positions_sync_out_doc_view, name='positionsSyncOutDocs'),
    url(r'^docs/positionSupportCountForBallotItem/',
        views_docs.position_support_count_for_ballot_item_doc_view, name='positionSupportCountForBallotItemDocs'),
    url(r'^docs/quickInfoRetrieve/$', views_docs.quick_info_retrieve_doc_view, name='quickInfoRetrieveDocs'),
    url(r'^docs/searchAll/$',
        views_docs.search_all_doc_view, name='searchAllDocs'),
    url(r'^docs/twitterIdentityRetrieve/$',
        views_docs.twitter_identity_retrieve_doc_view, name='twitterIdentityRetrieveDocs'),
    url(r'^docs/twitterSignInRequestAccessToken/$',
        views_docs.twitter_sign_in_request_access_token_doc_view, name='twitterSignInRequestAccessTokenDocs'),
    url(r'^docs/twitterSignInRequestVoterInfo/$',
        views_docs.twitter_sign_in_request_voter_info_doc_view, name='twitterSignInRequestVoterInfoDocs'),
    url(r'^docs/twitterSignInRetrieve/$',
        views_docs.twitter_sign_in_retrieve_doc_view, name='twitterSignInRetrieveDocs'),
    url(r'^docs/twitterSignInStart/$', views_docs.twitter_sign_in_start_doc_view, name='twitterSignInStartDocs'),
    url(r'^docs/twitterRetrieveIdsIFollow/$',
        views_docs.twitter_retrieve_ids_i_follow_doc_view, name='twitterRetrieveIdsIFollowDocs'),
    url(r'^docs/voterAddressRetrieve/$', views_docs.voter_address_retrieve_doc_view, name='voterAddressRetrieveDocs'),
    url(r'^docs/voterAddressSave/$', views_docs.voter_address_save_doc_view, name='voterAddressSaveDocs'),
    url(r'^docs/voterAllPositionsRetrieve/$',
        views_docs.voter_all_positions_retrieve_doc_view, name='voterAllPositionsRetrieveDocs'),
    url(r'^docs/voterAllBookmarksStatusRetrieve/$',
        views_docs.voter_all_bookmarks_status_retrieve_doc_view, name='voterAllBookmarksStatusRetrieveDocs'),
    url(r'^docs/voterBallotItemsRetrieve/$',
        views_docs.voter_ballot_items_retrieve_doc_view, name='voterBallotItemsRetrieveDocs'),
    url(r'^docs/voterBallotItemsRetrieveFromGoogleCivic/$',
        views_docs.voter_ballot_items_retrieve_from_google_civic_doc_view,
        name='voterBallotItemsRetrieveFromGoogleCivicDocs'),
    url(r'^docs/voterBallotListRetrieve/$', views_docs.voter_ballot_list_retrieve_doc_view,
        name='voterBallotListRetrieveDocs'),
    url(r'^docs/voterBookmarkOffSave/$', views_docs.voter_bookmark_off_save_doc_view, name='voterBookmarkOffSaveDocs'),
    url(r'^docs/voterBookmarkOnSave/$', views_docs.voter_bookmark_on_save_doc_view, name='voterBookmarkOnSaveDocs'),
    url(r'^docs/voterBookmarkStatusRetrieve/$',
        views_docs.voter_bookmark_status_retrieve_doc_view, name='voterBookmarkStatusRetrieveDocs'),
    url(r'^docs/voterCount/$', views_docs.voter_count_doc_view, name='voterCountDocs'),
    url(r'^docs/voterCreate/$', views_docs.voter_create_doc_view, name='voterCreateDocs'),
    url(r'^docs/voterEmailAddressRetrieve/$',
        views_docs.voter_email_address_retrieve_doc_view, name='voterEmailAddressRetrieveDocs'),
    url(r'^docs/voterEmailAddressSave/$',
        views_docs.voter_email_address_save_doc_view, name='voterEmailAddressSaveDocs'),
    url(r'^docs/voterEmailAddressSignIn/$',
        views_docs.voter_email_address_sign_in_doc_view, name='voterEmailAddressSignInDocs'),
    url(r'^docs/voterEmailAddressVerify/$',
        views_docs.voter_email_address_verify_doc_view, name='voterEmailAddressVerifyDocs'),
    url(r'^docs/voterFacebookSaveToCurrentAccount/$',
        views_docs.voter_facebook_save_to_current_account_doc_view, name='voterFacebookSaveToCurrentAccountDocs'),
    url(r'^docs/voterFacebookSignInRetrieve/$',
        views_docs.voter_facebook_sign_in_retrieve_doc_view, name='voterFacebookSignInRetrieveDocs'),
    url(r'^docs/voterFacebookSignInSave/$',
        views_docs.voter_facebook_sign_in_save_doc_view, name='voterFacebookSignInSaveDocs'),
    url(r'^docs/voterGuidePossibilityRetrieve/$',
        views_docs.voter_guide_possibility_retrieve_doc_view, name='voterGuidePossibilityRetrieveDocs'),
    url(r'^docs/voterGuidePossibilitySave/$',
        views_docs.voter_guide_possibility_save_doc_view, name='voterGuidePossibilitySaveDocs'),
    url(r'^docs/voterGuidesFollowedRetrieve/$',
        views_docs.voter_guides_followed_retrieve_doc_view, name='voterGuidesFollowedRetrieveDocs'),
    url(r'^docs/voterGuidesFollowedByOrganizationRetrieve/$',
        views_docs.voter_guides_followed_by_organization_retrieve_doc_view,
        name='voterGuidesFollowedByOrganizationRetrieveDocs'),
    url(r'^docs/voterGuidesIgnoredRetrieve/$',
        views_docs.voter_guides_ignored_retrieve_doc_view, name='voterGuidesIgnoredRetrieveDocs'),
    url(r'^docs/voterGuidesSyncOut/$', views_docs.voter_guides_sync_out_doc_view, name='voterGuidesSyncOutDocs'),
    url(r'^docs/voterGuidesToFollowRetrieve/$',
        views_docs.voter_guides_to_follow_retrieve_doc_view, name='voterGuidesToFollowRetrieveDocs'),
    url(r'^docs/voterLocationRetrieveFromIP/$',
        views_docs.voter_location_retrieve_from_ip_doc_view, name='voterLocationRetrieveFromIPDocs'),
    url(r'^docs/voterMergeTwoAccounts/$',
        views_docs.voter_merge_two_accounts_doc_view, name='voterMergeTwoAccountsDocs'),
    url(r'^docs/voterPhotoSave/$', views_docs.voter_photo_save_doc_view, name='voterPhotoSaveDocs'),
    url(r'^docs/voterOpposingSave/$', views_docs.voter_opposing_save_doc_view, name='voterOpposingSaveDocs'),
    url(r'^docs/voterPositionRetrieve/$',
        views_docs.voter_position_retrieve_doc_view, name='voterPositionRetrieveDocs'),
    url(r'^docs/voterPositionCommentSave/$',
        views_docs.voter_position_comment_save_doc_view, name='voterPositionCommentSaveDocs'),
    url(r'^docs/voterPositionLikeOffSave/$',
        views_docs.voter_position_like_off_save_doc_view, name='voterPositionLikeOffSaveDocs'),
    url(r'^docs/voterPositionLikeOnSave/$',
        views_docs.voter_position_like_on_save_doc_view, name='voterPositionLikeOnSaveDocs'),
    url(r'^docs/voterPositionLikeStatusRetrieve/$',
        views_docs.voter_position_like_status_retrieve_doc_view, name='voterPositionLikeStatusRetrieveDocs'),
    url(r'^docs/voterPositionVisibilitySave/$',
        views_docs.voter_position_visibility_save_doc_view, name='voterPositionVisibilitySaveDocs'),
    url(r'^docs/voterRetrieve/$', views_docs.voter_retrieve_doc_view, name='voterRetrieveDocs'),
    url(r'^docs/voterSignOut/$', views_docs.voter_sign_out_doc_view, name='voterSignOutDocs'),
    url(r'^docs/voterSplitIntoTwoAccounts/$',
        views_docs.voter_split_into_two_accounts_doc_view, name='voterSplitIntoTwoAccountsDocs'),
    url(r'^docs/voterStopOpposingSave/$',
        views_docs.voter_stop_opposing_save_doc_view, name='voterStopOpposingSaveDocs'),
    url(r'^docs/voterStopSupportingSave/$',
        views_docs.voter_stop_supporting_save_doc_view, name='voterStopSupportingSaveDocs'),
    url(r'^docs/voterSupportingSave/$', views_docs.voter_supporting_save_doc_view, name='voterSupportingSaveDocs'),
    url(r'^docs/voterTwitterSaveToCurrentAccount/$',
        views_docs.voter_twitter_save_to_current_account_doc_view, name='voterTwitterSaveToCurrentAccountDocs'),
    url(r'^docs/voterUpdate/$', views_docs.voter_update_doc_view, name='voterUpdateDocs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
