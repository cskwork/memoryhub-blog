---
title: "Windows Excel 대괄호 파일명 문제 - 2025년 5월"
date: 2025-06-11T22:16:30+09:00
slug: "682-Windows-Excel-대괄호-파일명-문제-2025년-5월"
original_url: "https://memoryhub.tistory.com/682"
tistory_id: 682
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
---

Microsoft Office의 2025년 5월 보안 업데이트로 인해 대괄호가 포함된 Excel 파일명에서 심각한 문제가 발생하고 있습니다. 이는 단순한 버그가 아닌 Microsoft의 설계 결정과 최근 보안 강화 조치가 결합된 복합적 문제입니다.

## 2025년 5월 중대한 변화: Office 보안 업데이트의 파급효과

**가장 중요한 발견사항**은 2025년 5월 13일 Microsoft Office 보안 업데이트(KB5002717 및 관련 패치)가 Office 2016, Office 2016-2021 C2R, Office 2021, Microsoft 365에서 대괄호가 포함된 파일명을 완전히 차단하기 시작했다는 점입니다.

독일의 Dennis F.가 2025년 5월 23일 보고한 바에 따르면, Excel이 이제 대괄호에서 파일명을 **절단**하여 처리합니다. 예를 들어 `[Test]Report.xlsx` 파일의 경우 Excel이 전체 파일명 대신 `Report.xlsx`만 찾으려 시도합니다. 이는 Office 365 Version 2504 Build 16.0.18730.20186과 Version 2505 Build 16.0.18827.20102에서 확인되었으며, 흥미롭게도 Windows 10 22H2의 Office 2016 32비트 MSI 버전에서는 문제가 발생하지 않습니다.

## 근본적 기술 원인: Excel의 설계 한계

Excel의 대괄호 문제는 **1990년대부터 지속된 설계적 제약**에서 비롯됩니다. Excel은 외부 워크북 참조에 대괄호를 구문 구분자로 사용합니다(`=[WorkbookName.xlsx]SheetName!CellReference`). 이로 인해 Excel은 파일명의 일부인 대괄호와 수식 구문의 대괄호를 구별할 수 없는 **근본적인 파싱 충돌**을 겪습니다.

Microsoft는 이를 공식적으로 "버그가 아닌 예상된 동작"으로 분류하고 있습니다. Microsoft 지원 문서에 따르면 `< > ? [ ] : | *` 문자들은 Excel 워크북 파일명에서 **금지된 문자**로 명시되어 있으며, 특히 피벗테이블이 포함된 파일에서 "데이터 원본 참조가 잘못되었습니다" 오류를 발생시킵니다.

## Windows 및 Office 업데이트의 구체적 영향

### 2024년 11월 Excel 보안 업데이트의 선행 신호

2024년 11월 12일 Excel 보안 업데이트(KB5002653)에서 **CVE-2024-49026부터 CVE-2024-49030까지** 5개의 Excel 원격 코드 실행 취약점이 수정되었습니다. 이 업데이트는 Excel의 파일 열기 메커니즘을 직접 수정했으며, 특수 문자가 포함된 파일 처리 방식에 영향을 미쳤습니다.

### Windows 11 24H2의 보안 강화

2024년 10월 1일부터 단계적으로 출시된 Windows 11 24H2는 **SMB 서명 요구사항 기본 활성화**와 **향상된 파일 시스템 보안**을 도입했습니다. 특히 KB5044284(10월 8일), KB5046617(11월 12일), KB5048667(12월 10일) 업데이트들이 파일 처리 보안을 대폭 강화했습니다.

### Microsoft Defender 및 Edge 보안 정책 변화

Microsoft Defender의 2024년 10월-11월 플랫폼 업데이트는 **더욱 적극적인 파일 스캔 알고리즘**을 도입했으며, "의심스러운 파일명 패턴" 감지 기능이 강화되었습니다. Microsoft Edge의 향상된 SmartScreen은 특수 문자가 포함된 파일을 더 엄격하게 분류하고 자동 차단하기 시작했습니다.

## 브라우저별 동작 차이와 다운로드 문제

### Internet Explorer의 고유한 문제점

Internet Explorer는 중복 다운로드 시 자동으로 `[1]`, `[2]` 등을 파일명에 추가합니다. 이는 **피벗테이블 자동 새로고침 기능을 완전히 마비**시키며 "file[1].yourPivotTableName is not valid" 오류를 발생시킵니다.

### 현대 브라우저들의 상대적 안정성

Chrome, Edge(Chromium), Firefox는 Content-Disposition 헤더를 통해 전달된 원본 파일명을 대부분 보존합니다. Firefox는 **가장 강력한 유니코드 지원**을 제공하며, Chrome과 Edge는 특정 시나리오에서 따옴표 관련 문제를 보이지만 대괄호 자체는 잘 처리합니다.

## 기업 환경에서의 심각한 파급효과

한 사용자는 다음과 같이 보고했습니다: "COBOL로 작성된 오래된 시스템이 대괄호가 포함된 파일을 자동 생성합니다. 구 버전 Office는 여전히 이 파일들에 접근할 수 있지만 365를 사용하는 사용자는 접근할 수 없습니다."

**기업 IT 관리자들이 직면한 문제들:**

- 레거시 시스템에서 생성된 기존 파일들에 대한 접근 불가
- 이메일 첨부파일의 중복 번호가 자동으로 대괄호로 추가됨
- 자동화된 보고 시스템의 중단
- 공유 드라이브의 기존 파일들 사용 불가

## 실용적 해결방안과 우회책

### 즉시 적용 가능한 임시 해결책

1. **파일명 변경**: 모든 대괄호를 제거한 후 Excel에서 열기
2. **브라우저 설정**: IE 다운로드 시 "열기" 대신 "저장" 사용
3. **브라우저 교체**: IE 대신 Chrome, Firefox, Edge 사용
4. **수동 파일 복사**: 파일을 데스크톱에 저장 후 이름 변경

### IT 관리자를 위한 시스템 레벨 해결책

1. **그룹 정책**: 대괄호 사용 금지 명명 규칙 구현
2. **파일 서버 스크립트**: 대괄호 포함 파일 자동 이름 변경
3. **브라우저 구성**: Office 파일 처리 시 IE를 기본값에서 제외
4. **버전 관리**: 레거시 파일 접근을 위한 구 Office 버전 유지

### 개발자를 위한 근본적 해결책

**서버 측 해결방안:**

- Content-Disposition 헤더를 "inline" 대신 "attachment"로 설정
- 파일명에서 대괄호 사전 제거
- URL 재작성을 통한 대괄호 생성 방지

**클라이언트 측 해결방안:**

- 파일 시스템 감시기를 통한 다운로드 파일 자동 이름 변경
- VBA 매크로를 통한 대괄호 감지 및 처리
- .NET 애플리케이션을 통한 자동화된 파일 처리

## Microsoft의 공식 입장과 향후 전망

Microsoft는 이 문제를 **"Excel 사양 외부의 동작"**으로 간주하고 있으며, 버그 수정보다는 사용자의 파일명 규칙 준수를 권장하고 있습니다. 공식 Microsoft 지원 문서는 대괄호를 명확히 "무효한 문자"로 분류하고 있으며, 이를 제거할 것을 권장합니다.

**OneDrive 및 Microsoft 365 연동:**  
Microsoft 365 앱들은 OneDrive 저장 시 대괄호가 포함된 파일을 **자동으로 이름을 변경**합니다. 이는 Microsoft가 일관되게 대괄호를 지원하지 않는 문자로 취급하고 있음을 보여줍니다.

## 결론: 근본적 해결을 위한 권고사항

이 문제는 단순한 기술적 버그가 아닌 **Excel의 근본적 아키텍처 설계 한계**입니다. 2025년 5월 보안 업데이트로 인해 문제가 심각해졌지만, 이는 30년 넘게 지속된 설계적 제약의 연장선에 있습니다.

**조직을 위한 권고사항:**

1. **단기**: 대괄호를 제외한 파일 명명 정책 즉시 구현
2. **중기**: 레거시 시스템의 파일 생성 로직 수정
3. **장기**: Excel 의존성을 줄이고 대안 솔루션 검토

**개발자를 위한 권고사항:**

1. 서버에서 파일 생성 시 대괄호 사용 금지
2. Content-Disposition 헤더 최적화
3. 클라이언트 측 파일명 검증 및 정제 로직 구현

**최종 판단**: Microsoft가 이를 의도된 동작으로 분류하고 있어 향후 수정 가능성이 낮으므로, 조직과 개발자는 Excel의 파일명 제약사항에 맞춰 시스템을 조정하는 것이 현실적입니다. 2025년 보안 업데이트로 인해 문제가 더욱 엄격해졌으므로, 기존 파일들의 일괄 이름 변경과 새로운 명명 규칙 도입이 시급합니다.

# 출처

[1] <https://support.microsoft.com/ko-kr/office/excel%EC%9D%80-%ED%8C%8C%EC%9D%BC-%EC%9D%B4%EB%A6%84-%EB%98%90%EB%8A%94-%ED%8F%B4%EB%8D%94-%EA%B2%BD%EB%A1%9C%EC%9D%98-%EC%9D%BC%EB%B6%80-%ED%8A%B9%EC%88%98-%EB%AC%B8%EC%9E%90%EB%A5%BC-%EC%99%84%EC%A0%84%ED%9E%88-%EC%A7%80%EC%9B%90%ED%95%98%EC%A7%80-%EC%95%8A%EC%8A%B5%EB%8B%88%EB%8B%A4-20728217-f08a-4d63-a741-821a14cec380>  
[2] <https://itsittime.tistory.com/3>  
[3] <https://uppogalxy.co.kr/%EC%97%91%EC%85%80-%EC%98%A4%EB%A5%98-%EC%9D%B4%EB%8F%99%ED%96%88%EA%B1%B0%EB%82%98-%EC%9D%B4%EB%A6%84%EC%9D%B4-%EB%B0%94%EB%80%8C%EC%97%88%EA%B1%B0%EB%82%98-%EC%82%AD%EC%A0%9C%EB%90%98%EC%97%88/>  
[4] <https://cms.dankook.ac.kr/web/archi/-21?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=804604>  
[5] <https://khuithelp.zendesk.com/hc/ko/articles/12792392923791-%EC%97%91%EC%85%80%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%ED%8C%8C%EC%9D%BC%EB%A7%8C-%EB%A5%BC-%EC%B0%BE%EC%9D%84-%EC%88%98-%EC%97%86%EC%8A%B5%EB%8B%88%EB%8B%A4-%ED%8C%8C%EC%9D%BC-%EC%9D%B4%EB%A6%84-%EB%B3%80%EA%B2%BD-%EC%9D%B4%EB%8F%99-%EC%82%AD%EC%A0%9C-%ED%99%95%EC%9D%B8-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%98%A4%EB%A5%98>  
[6] <https://hope.pe.kr/464>  
[7] <https://answers.microsoft.com/ko-kr/msoffice/forum/all/ms%EC%98%A4%ED%94%BC%EC%8A%A4/698738c2-42b7-4364-b169-81bd451c5983>  
[8] <https://cms.dankook.ac.kr/web/archi/-21?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=804604>  
[9] <https://www.youtube.com/shorts/cXwbt7ya6fs>  
[10] <https://4ddig.tenorshare.com/kr/office-recovery/fix-xlsx-file-cannot-be-opened.html>
