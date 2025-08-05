ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# -------------------------------
# 기본 설정: 미러 설정 및 시간대
# -------------------------------
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
ENV SHELL=/bin/bash
SHELL ["/bin/bash", "-c"]

RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://mirror.kakao.com/ubuntu|g' /etc/apt/sources.list && \
    sed -i 's|http://security.ubuntu.com/ubuntu|http://mirror.kakao.com/ubuntu|g' /etc/apt/sources.list && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get update && \
    apt-get install -y --no-install-recommends tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    rm -rf /var/lib/apt/lists/*

# -------------------------------
# 필수 시스템 패키지 설치
# -------------------------------
	RUN apt-get update && apt-get install -y --no-install-recommends \
    # 기본 시스템 유틸리티
    sudo apt-utils wget curl git zsh net-tools openssh-client htop x11-apps xauth at \
    build-essential cmake pkg-config \
    # 오디오/비디오 및 입력 장치
    v4l-utils ffmpeg usbutils alsa-utils portaudio19-dev pulseaudio \
    # Python 관련 개발 도구
    python3-dev python3-pip python3-venv python3-tk \
    # GUI 라이브러리
    libgtk2.0-dev libgtk-3-dev libgl1-mesa-glx libgl1-mesa-dev libglu1-mesa-dev \
    libglfw3-dev \
    # X11 관련 라이브러리
    libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
    libxcb-randr0 libxcb-render-util0 libxkbcommon-x11-0 libxcb-cursor0 \
    # USB 및 인증 관련
    libssl-dev libusb-1.0-0-dev libudev-dev udev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# -------------------------------
# Python 패키지 설치
# -------------------------------
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir \
    # 기본 유틸리티 및 수학/통계
    "numpy<1.24" pandas scipy tqdm typing-extensions \
    # 시각화
    matplotlib plotly pyvista dash dash-bootstrap-components \
    # 머신러닝/딥러닝
    scikit-learn scikit-image \
    torch torchvision torchtext torchaudio torchsummary \
	lightning \
	timm albumentations pycocotools transforms3d pyquaternion lap \
    kornia kornia_moons \
    ultralytics segment-anything \
    opencv-python "imutils==0.5.4" \
    # MLOps 도구
    wandb mlflow tensorboard gradio \
    # 웹 서버 / API 프레임워크
    fastapi uvicorn "tenacity==8.3.0"

# -------------------------------
# Python 테스트 및 분석 도구
# -------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-flake8-blind-except python3-flake8-class-newline \
    python3-flake8-deprecated python3-mypy \
    python3-pytest python3-pytest-cov python3-pytest-mock \
    python3-pytest-repeat python3-pytest-rerunfailures \
    python3-pytest-runner python3-pytest-timeout \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# -------------------------------
# 사용자 생성 및 설정
# -------------------------------
ARG USER_NAME
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN groupadd --gid ${USER_GID} ${USER_NAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USER_NAME} && \
    echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER_NAME} && \
    echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    usermod -a -G video ${USER_NAME} && \
    chmod 0440 /etc/sudoers.d/${USER_NAME}

USER ${USER_NAME}

# -------------------------------
# oh-my-zsh 및 zsh 플러그인 설정
# -------------------------------
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git   ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k && \
    git clone https://github.com/supercrabtree/k.git                   ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/k && \
    git clone https://github.com/zsh-users/zsh-autosuggestions.git     ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-completions.git         ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-completions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

COPY ./.zshrc ./.p10k.zsh /home/${USER_NAME}
ENV SHELL=/bin/zsh

USER root
RUN chown ${USER_NAME}:${USER_NAME} /home/${USER_NAME}/.zshrc /home/${USER_NAME}/.p10k.zsh

USER ${USER_NAME}
