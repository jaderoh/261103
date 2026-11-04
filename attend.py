import json
import os
from datetime import datetime

# 데이터 저장 파일
DATA_FILE = "attendance.json"

def load_data():
    """저장된 출석 데이터 불러오기"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    """출석 데이터 저장하기"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_attendance(date, name):
    """출석 기록 추가"""
    data = load_data()
    
    # 날짜 형식 검증 (YYYY-MM-DD)
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ 날짜 형식이 잘못되었습니다. (형식: YYYY-MM-DD)")
        return
    
    # 이름이 비어있는지 확인
    if not name.strip():
        print("❌ 이름을 입력해주세요.")
        return
    
    # 날짜별로 이름 추가
    if date not in data:
        data[date] = []
    
    if name in data[date]:
        print(f"⚠️  {date}에 {name}님은 이미 출석 기록이 있습니다.")
        return
    
    data[date].append(name)
    save_data(data)
    print(f"✅ {date}에 {name}님 출석이 기록되었습니다.")

def view_all():
    """전체 출석 목록 보기"""
    data = load_data()
    
    if not data:
        print("📋 기록된 출석이 없습니다.")
        return
    
    print("\n" + "="*50)
    print("📋 스터디 출석부")
    print("="*50)
    
    # 날짜순으로 정렬
    for date in sorted(data.keys()):
        names = data[date]
        print(f"\n📅 {date} ({len(names)}명)")
        for i, name in enumerate(names, 1):
            print(f"   {i}. {name}")
    
    print("\n" + "="*50 + "\n")

def view_by_date(date):
    """특정 날짜의 출석 목록 보기"""
    data = load_data()
    
    if date not in data:
        print(f"📋 {date}에 기록된 출석이 없습니다.")
        return
    
    names = data[date]
    print(f"\n📅 {date} 출석 현황 ({len(names)}명)")
    print("-" * 30)
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")
    print()

def view_by_person(name):
    """특정 사람의 출석 기록 보기"""
    data = load_data()
    
    attendance_dates = []
    for date, names in data.items():
        if name in names:
            attendance_dates.append(date)
    
    if not attendance_dates:
        print(f"📋 {name}님의 출석 기록이 없습니다.")
        return
    
    print(f"\n👤 {name}님의 출석 기록 ({len(attendance_dates)}회)")
    print("-" * 30)
    for i, date in enumerate(sorted(attendance_dates), 1):
        print(f"{i}. {date}")
    print()

def delete_attendance(date, name):
    """출석 기록 삭제"""
    data = load_data()
    
    if date not in data or name not in data[date]:
        print(f"❌ {date}에 {name}님의 출석 기록이 없습니다.")
        return
    
    data[date].remove(name)
    
    # 해당 날짜에 아무도 없으면 날짜 삭제
    if not data[date]:
        del data[date]
    
    save_data(data)
    print(f"🗑️  {date}의 {name}님 출석 기록이 삭제되었습니다.")

def show_menu():
    """메뉴 표시"""
    print("\n" + "="*50)
    print("🎓 스터디 출석부 프로그램")
    print("="*50)
    print("1. 출석 기록 추가")
    print("2. 전체 출석 목록 보기")
    print("3. 특정 날짜 출석 보기")
    print("4. 특정 사람 출석 기록 보기")
    print("5. 출석 기록 삭제")
    print("6. 종료")
    print("="*50)

def main():
    """메인 프로그램"""
    while True:
        show_menu()
        choice = input("선택: ").strip()
        
        if choice == "1":
            date = input("날짜 입력 (YYYY-MM-DD): ").strip()
            name = input("이름 입력: ").strip()
            add_attendance(date, name)
        
        elif choice == "2":
            view_all()
        
        elif choice == "3":
            date = input("날짜 입력 (YYYY-MM-DD): ").strip()
            view_by_date(date)
        
        elif choice == "4":
            name = input("이름 입력: ").strip()
            view_by_person(name)
        
        elif choice == "5":
            date = input("날짜 입력 (YYYY-MM-DD): ").strip()
            name = input("이름 입력: ").strip()
            delete_attendance(date, name)
        
        elif choice == "6":
            print("👋 프로그램을 종료합니다.")
            break
        
        else:
            print("❌ 잘못된 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()


//memo 261104**
