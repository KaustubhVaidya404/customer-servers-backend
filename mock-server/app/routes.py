from flask import Blueprint, request, jsonify
import logging
from app.services.customer_service import (
    get_all_customers,
    get_customer_by_id
)
from app.utils.pagination import paginate

logger = logging.getLogger(__name__)

customer_bp = Blueprint("customers", __name__)

# Health check
@customer_bp.route("/api/health", methods=["GET"])
def health():
    logger.debug("Health check requested")
    return jsonify({"status": "ok"}), 200


# Get paginated customers
@customer_bp.route("/api/customers", methods=["GET"])
def customers():
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))
        logger.info(f"Paginated customers requested: page={page}, limit={limit}")

        customers = get_all_customers()
        result = paginate(customers, page, limit)
        logger.info(f"Returning {len(result.get('data', []))} customers")

        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error fetching customers: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500


# Get single customer
@customer_bp.route("/api/customers/<customer_id>", methods=["GET"])
def customer(customer_id):
    logger.info(f"Customer detail requested for ID: {customer_id}")
    customer = get_customer_by_id(customer_id)

    if not customer:
        logger.warning(f"Customer with ID {customer_id} not found")
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer), 200