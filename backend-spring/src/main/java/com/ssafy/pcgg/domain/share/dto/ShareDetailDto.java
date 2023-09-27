package com.ssafy.pcgg.domain.share.dto;

import java.time.LocalDateTime;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class ShareDetailDto {
	private Long id;
	private Long userId;
	private Long quoteId;
	private String title;
	private String content;
	private String summary;
	private LocalDateTime createdAt;
	private Long likeCnt;
	private Long dislikeCnt;
}
