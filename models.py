"""
여행 큐레이터 에이전트의 데이터 모델
"""

from pydantic import BaseModel, Field
from enum import Enum

class TravelProfile(BaseModel):
    name: str = Field(description="사용자 이름")
    travel_style: str = Field(description="여행 스타일 (예: 액티비티, 힐링, 맛집 탐방, 문화유적)")
    preferred_transport: str = Field(description="선호 이동 수단 (예: 대중교통, 렌터카, 도보)")
    budget_range: str = Field(description="일일 예상 예산 범위 (예: 저예산, 중급, 럭셔리)")

class Place(BaseModel):
    place_name: str = Field(description="장소 명칭")
    category: str = Field(description="장소 카테고리 (음식점, 관광지, 숙소 등)")
    description: str = Field(description="장소에 대한 간단한 설명")
    estimated_cost: int = Field(description="예상 비용 (원 단위)")

class TravelPlan(BaseModel):
    destination: str = Field(description="여행 목적지")
    duration_days: int = Field(description="여행 기간 (박/일)")
    itinerary: str = Field(description="상세 일정 내용 (마크다운 형식)")
    total_estimated_budget: int = Field(description="총 예상 비용")

class TravelRegion(Enum):
    SEOUL = "서울"
    JEJU = "제주"
    BUSAN = "부산"
    GANGWON = "강원"
    GYEONGJU = "경주"