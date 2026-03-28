from agents import get_travel_curator_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 모델 설정 (기존 설정 유지)
model = ChatGroq(
    model="openai/gpt-oss-20b",
)

# 여행 큐레이터 에이전트 생성
travel_curator_agent = get_travel_curator_agent(model)

# 실행 예시: 사용자 정보 등록 및 여행 계획 요청
print("--- 여행 큐레이터 가동 중 ---")

result = travel_curator_agent.invoke({
    "messages": [
        {
            "role": "user", 
            "content": "내 이름은 김여행이야. 나는 액티비티보다는 조용한 카페나 풍경 위주의 힐링 여행을 좋아해. 이동은 주로 렌터카를 이용하고 예산은 적당히 여유로운 편이야. 이번에 제주도 2박 3일 여행을 가려고 하는데, 첫날 일정 위주로 계획을 짜주고 저장해줘!"}
    ]
})

print(result)
print(result['messages'][-1].content)