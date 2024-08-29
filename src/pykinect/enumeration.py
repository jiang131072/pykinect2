"""Kinect for Windows SDK 2.0 CXX Enumerations
https://learn.microsoft.com/en-us/previous-versions/windows/kinect/dn758672(v=ieb.10)
"""

from ctypes.wintypes import INT
from enum import IntEnum


class _Enum(IntEnum):
    @classmethod
    def Count(cls):
        return len(cls.__members__)

    dtype = INT


class Activity(_Enum):
    EyeLeftClosed = 0
    EyeRightClosed = 1
    MouthOpen = 2
    MouthMoved = 3
    LookingAway = 4


class Appearance(_Enum):
    WearingGlasses = 0


class AudioBeamMode(_Enum):
    Automatic = 0
    Manual = 1


class ColorImageFormat(_Enum):
    None_ = 0
    Rgba = 1
    Yuv = 2
    Bgra = 3
    Bayer = 4
    Yuy2 = 5


class DetectionResult(_Enum):
    Unknown = 0
    No = 1
    Maybe = 2
    Yes = 3


class KinectEngagementMode(_Enum):
    None_ = 0
    SystemOnePerson = 1
    SystemTwoPerson = 2
    ManualOnePerson = 3
    ManualTwoPerson = 4


class Expression(_Enum):
    Neutral = 0
    Happy = 1


class FrameCapturedStatus(_Enum):
    Unknown = 0
    Queued = 1
    Dropped = 2


class FrameEdges(_Enum):
    None_ = 0
    Right = 0x1
    Left = 0x2
    Top = 0x4
    Bottom = 0x8


class FrameSourceTypes(_Enum):
    None_ = 0
    Color = 0x1
    Infrared = 0x2
    LongExposureInfrared = 0x4
    Depth = 0x8
    BodyIndex = 0x10
    Body = 0x20
    Audio = 0x40


class HandState(_Enum):
    Unknown = 0
    NotTracked = 1
    Open = 2
    Closed = 3
    Lasso = 4


class HandType(_Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2


class JointType(_Enum):
    SpineBase = 0
    SpineMid = 1
    Neck = 2
    Head = 3
    ShoulderLeft = 4
    ElbowLeft = 5
    WristLeft = 6
    HandLeft = 7
    ShoulderRight = 8
    ElbowRight = 9
    WristRight = 10
    HandRight = 11
    HipLeft = 12
    KneeLeft = 13
    AnkleLeft = 14
    FootLeft = 15
    HipRight = 16
    KneeRight = 17
    AnkleRight = 18
    FootRight = 19
    SpineShoulder = 20
    HandTipLeft = 21
    ThumbLeft = 22
    HandTipRight = 23
    ThumbRight = 24


class KinectAudioCalibrationState(_Enum):
    Unknown = 0
    CalibrationRequired = 1
    Calibrated = 2


class KinectCapabilities(_Enum):
    None_ = 0
    Vision = 0x1
    Audio = 0x2
    Face = 0x4
    Expressions = 0x8
    Gamechat = 0x10


class KinectGestureSettings(_Enum):
    None_ = 0
    Tap = 0x1
    ManipulationTranslateX = 0x40
    ManipulationTranslateY = 0x80
    ManipulationTranslateRailsX = 0x100
    ManipulationTranslateRailsY = 0x200
    ManipulationScale = 0x800
    ManipulationTranslateInertia = 0x1000
    KinectHold = 0x10000


class KinectHoldingState(_Enum):
    Started = 0
    Completed = 1
    Canceled = 2


class KinectInteractionMode(_Enum):
    Normal = 0
    Off = 1
    Media = 2


class PointerDeviceType(_Enum):
    Touch = 0
    Pen = 1
    Mouse = 2
    Kinect = 3


class TrackingConfidence(_Enum):
    Low = 0
    High = 1


class TrackingState(_Enum):
    NotTracked = 0
    Inferred = 1
    Tracked = 2


class FaceAlignmentQuality(_Enum):
    High = 0
    Low = 1


class FaceFrameFeatures(_Enum):
    None_ = 0
    BoundingBoxInInfraredSpace = 0x1
    PointsInInfraredSpace = 0x2
    BoundingBoxInColorSpace = 0x4
    PointsInColorSpace = 0x8
    RotationOrientation = 0x10
    Happy = 0x20
    RightEyeClosed = 0x40
    LeftEyeClosed = 0x80
    MouthOpen = 0x100
    MouthMoved = 0x200
    LookingAway = 0x400
    Glasses = 0x800
    FaceEngagement = 0x1000


class FaceModelBuilderCaptureStatus(_Enum):
    GoodFrameCapture = 0
    OtherViewsNeeded = 1
    LostFaceTrack = 2
    FaceTooFar = 3
    FaceTooNear = 4
    MovingTooFast = 5
    SystemError = 6


class FaceModelBuilderCollectionStatus(_Enum):
    Complete = 0
    MoreFramesNeeded = 0x1
    FrontViewFramesNeeded = 0x2
    LeftViewsNeeded = 0x4
    RightViewsNeeded = 0x8
    TiltedUpViewsNeeded = 0x10


class FacePointType(_Enum):
    EyeLeft = 0
    EyeRight = 1
    Nose = 2
    MouthCornerLeft = 3
    MouthCornerRight = 4


class FaceProperty(_Enum):
    Happy = 0
    Engaged = 1
    WearingGlasses = 2
    LeftEyeClosed = 3
    RightEyeClosed = 4
    MouthOpen = 5
    MouthMoved = 6
    LookingAway = 7


class FaceShapeAnimations(_Enum):
    JawOpen = 0
    LipPucker = 1
    JawSlideRight = 2
    LipStretcherRight = 3
    LipStretcherLeft = 4
    LipCornerPullerLeft = 5
    LipCornerPullerRight = 6
    LipCornerDepressorLeft = 7
    LipCornerDepressorRight = 8
    LeftcheekPuff = 9
    RightcheekPuff = 10
    LefteyeClosed = 11
    RighteyeClosed = 12
    RighteyebrowLowerer = 13
    LefteyebrowLowerer = 14
    LowerlipDepressorLeft = 15
    LowerlipDepressorRight = 16


class FaceShapeDeformations(_Enum):
    PCA01 = 0
    PCA02 = 1
    PCA03 = 2
    PCA04 = 3
    PCA05 = 4
    PCA06 = 5
    PCA07 = 6
    PCA08 = 7
    PCA09 = 8
    PCA10 = 9
    Chin03 = 10
    Forehead00 = 11
    Cheeks02 = 12
    Cheeks01 = 13
    MouthBag01 = 14
    MouthBag02 = 15
    Eyes02 = 16
    MouthBag03 = 17
    Forehead04 = 18
    Nose00 = 19
    Nose01 = 20
    Nose02 = 21
    MouthBag06 = 22
    MouthBag05 = 23
    Cheeks00 = 24
    Mask03 = 25
    Eyes03 = 26
    Nose03 = 27
    Eyes08 = 28
    MouthBag07 = 29
    Eyes00 = 30
    Nose04 = 31
    Mask04 = 32
    Chin04 = 33
    Forehead05 = 34
    Eyes06 = 35
    Eyes11 = 36
    Nose05 = 37
    Mouth07 = 38
    Cheeks08 = 39
    Eyes09 = 40
    Mask10 = 41
    Mouth09 = 42
    Nose07 = 43
    Nose08 = 44
    Cheeks07 = 45
    Mask07 = 46
    MouthBag09 = 47
    Nose06 = 48
    Chin02 = 49
    Eyes07 = 50
    Cheeks10 = 51
    Rim20 = 52
    Mask22 = 53
    MouthBag15 = 54
    Chin01 = 55
    Cheeks04 = 56
    Eyes17 = 57
    Cheeks13 = 58
    Mouth02 = 59
    MouthBag12 = 60
    Mask19 = 61
    Mask20 = 62
    Forehead06 = 63
    Mouth13 = 64
    Mask25 = 65
    Chin05 = 66
    Cheeks20 = 67
    Nose09 = 68
    Nose10 = 69
    MouthBag27 = 70
    Mouth11 = 71
    Cheeks14 = 72
    Eyes16 = 73
    Mask29 = 74
    Nose15 = 75
    Cheeks11 = 76
    Mouth16 = 77
    Eyes19 = 78
    Mouth17 = 79
    MouthBag36 = 80
    Mouth15 = 81
    Cheeks25 = 82
    Cheeks16 = 83
    Cheeks18 = 84
    Rim07 = 85
    Nose13 = 86
    Mouth18 = 87
    Cheeks19 = 88
    Rim21 = 89
    Mouth22 = 90
    Nose18 = 91
    Nose16 = 92
    Rim22 = 93


class HighDetailFacePoints(_Enum):
    EyeLeft = 0
    LefteyeInnercorner = 210
    LefteyeOutercorner = 469
    LefteyeMidtop = 241
    LefteyeMidbottom = 1104
    RighteyeInnercorner = 843
    RighteyeOutercorner = 1117
    RighteyeMidtop = 731
    RighteyeMidbottom = 1090
    LefteyebrowInner = 346
    LefteyebrowOuter = 140
    LefteyebrowCenter = 222
    RighteyebrowInner = 803
    RighteyebrowOuter = 758
    RighteyebrowCenter = 849
    MouthLeftcorner = 91
    MouthRightcorner = 687
    MouthUpperlipMidtop = 19
    MouthUpperlipMidbottom = 1072
    MouthLowerlipMidtop = 10
    MouthLowerlipMidbottom = 8
    NoseTip = 18
    NoseBottom = 14
    NoseBottomleft = 156
    NoseBottomright = 783
    NoseTop = 24
    NoseTopleft = 151
    NoseTopright = 772
    ForeheadCenter = 28
    LeftcheekCenter = 412
    RightcheekCenter = 933
    Leftcheekbone = 458
    Rightcheekbone = 674
    ChinCenter = 4
    LowerjawLeftend = 1307
    LowerjawRightend = 1327
