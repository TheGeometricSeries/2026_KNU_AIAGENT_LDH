from langchain_core.tools import tool
from models import TravelProfile, TravelPlan, Place
from mock_db import get_store

@tool
def save_travel_profile(
    name: str,
    travel_style: str,
    preferred_transport: str,
    budget_range: str
    ) -> TravelProfile:
    """사용자의 여행 성향과 선호도를 저장합니다."""

    profile = TravelProfile(
        name=name,
        travel_style=travel_style,
        preferred_transport=preferred_transport,
        budget_range=budget_range
    )
    store = get_store()
    store["profile"].append(profile)

    return profile

@tool
def save_itinerary(
    destination: str,
    duration_days: int,
    itinerary: str,
    total_estimated_budget: int
    ) -> TravelPlan:
    """최종 결정된 여행 일정을 데이터베이스에 저장합니다."""

    plan = TravelPlan(
        destination=destination,
        duration_days=duration_days,
        itinerary=itinerary,
        total_estimated_budget=total_estimated_budget
    )
    store = get_store()
    store["saved_itineraries"].append(plan)

    return plan

@tool
def get_user_travel_info(
    place_name:str,
    category:str,
    description:str,
    estimated_cost:int,
    ) -> Place:
    """저장된 사용자의 성향과 과거 여행 계획들을 조회합니다."""

    history = Place(
        place_name=place_name,
        category=category,
        description=description,
        estimated_cost=estimated_cost
    )
    store = get_store()
    store["profile"].append(history)

    return history