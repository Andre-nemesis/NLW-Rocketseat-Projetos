from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint("trip_routes", __name__)

# import controllers
from src.controllers.link_creator import LinkCreator
from src.controllers.trip_creator import TripCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder

from src.controllers.participants_creator import ParticipantCreator
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.controllers.participant_finder import ParticipantFinder

# import repositories
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

# import connections
from src.models.settings.db_connection_handler import db_connection_handler


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trips(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    controller = LinkCreator(link_repository)

    response = controller.create_link(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    controller = LinkFinder(link_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)
    email_repository = EmailsToInviteRepository(conn)

    controller = ParticipantCreator(participant_repository, email_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)

    controller = ActivityCreator(activity_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def find_activity_from_trip(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)

    controller = ActivityFinder(activity_repository)

    response = controller.find_activity_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)

    response = controller.find_participant_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/participants/<participantsId>/confirm", methods=["PATCH"])
def confirm_participant(participantsId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(participants_repository)

    response = controller.participant_confirm(participantsId)

    return jsonify(response["body"]), response["status_code"]
