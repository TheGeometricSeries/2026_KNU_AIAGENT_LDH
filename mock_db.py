_store: dict = {
    "profile": [],              # 사용자 여행 성향
    "saved_itineraries": [],    # 생성된 여행 일정
    "wishlist": [],             # 가고 싶은 장소들
}

def get_store():
    return _store