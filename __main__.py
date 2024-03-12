import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help

session = script_help.get_api_session()

resource_vendor = script_help.get_resource_context_details().attributes['CS_GenericResource.Vendor']
resource_model = script_help.get_resource_context_details().attributes['CS_GenericResource.Model']
resource_user = script_help.get_resource_context_details().attributes['AbSwitch.Backup User']
resource_password = script_help.get_resource_context_details().attributes['AbSwitch.Backup Password']
resource_fullname = script_help.get_resource_context_details().fullname

session.WriteMessageToReservationOutput(
    reservationId=script_help.get_reservation_context_details().id,
    message='the resource vendor is {}'.format(resource_vendor)
)

session.WriteMessageToReservationOutput(
    reservationId=script_help.get_reservation_context_details().id,
    message='the resource model is {}'.format(resource_model)
)

session.WriteMessageToReservationOutput(
    reservationId=script_help.get_reservation_context_details().id,
    message='the resource User is {}'.format(resource_user)
)

session.WriteMessageToReservationOutput(
    reservationId=script_help.get_reservation_context_details().id,
    message='the resource password is {}'.format(resource_password)
)

session.WriteMessageToReservationOutput(
    reservationId=script_help.get_reservation_context_details().id,
    message='the resource fullname is {}'.format(resource_fullname)
)