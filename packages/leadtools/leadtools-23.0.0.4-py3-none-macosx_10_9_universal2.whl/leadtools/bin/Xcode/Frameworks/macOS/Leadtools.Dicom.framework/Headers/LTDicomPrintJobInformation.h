// *************************************************************
// Copyright (c) 1991-2024 LEAD Technologies, Inc.
// All Rights Reserved.
// *************************************************************
//
//  LTDicomPrintJobInformation.h
//  Leadtools.Dicom
//

NS_ASSUME_NONNULL_BEGIN

NS_CLASS_AVAILABLE(10_10, 8_0)
@interface LTDicomPrintJobInformation : NSObject

@property (nonatomic, copy, nullable) NSString *executionStatus;
@property (nonatomic, copy, nullable) NSString *executionStatusInfo;
@property (nonatomic, copy, nullable) NSString *printPriority;
@property (nonatomic, copy, nullable) NSString *creationDate;
@property (nonatomic, copy, nullable) NSString *creationTime;
@property (nonatomic, copy, nullable) NSString *printerName;
@property (nonatomic, copy, nullable) NSString *originator;

@end

NS_ASSUME_NONNULL_END
