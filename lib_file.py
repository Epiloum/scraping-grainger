def write_to_file(file_path, content):
    try:
        # 파일을 쓰기 모드로 열기 (파일이 없으면 생성됨)
        with open(file_path, 'a+') as f:
            # 파일에 데이터 쓰기
            f.write(content)
        
        # 파일이 성공적으로 쓰여졌음을 출력
        print(f"파일 '{file_path}'이 성공적으로 생성되었습니다.")
    
    except Exception as e:
        print(f"파일 쓰기 중 오류가 발생했습니다: {e}")