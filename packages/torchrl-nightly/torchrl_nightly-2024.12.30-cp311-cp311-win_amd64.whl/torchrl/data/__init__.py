# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from .map import (
    BinaryToDecimal,
    HashToInt,
    MCTSForest,
    QueryModule,
    RandomProjectionHash,
    SipHash,
    TensorDictMap,
    TensorMap,
    Tree,
)
from .postprocs import MultiStep
from .replay_buffers import (
    Flat2TED,
    FlatStorageCheckpointer,
    H5Combine,
    H5Split,
    H5StorageCheckpointer,
    ImmutableDatasetWriter,
    LazyMemmapStorage,
    LazyTensorStorage,
    ListStorage,
    ListStorageCheckpointer,
    Nested2TED,
    NestedStorageCheckpointer,
    PrioritizedReplayBuffer,
    PrioritizedSampler,
    PrioritizedSliceSampler,
    RandomSampler,
    RemoteTensorDictReplayBuffer,
    ReplayBuffer,
    ReplayBufferEnsemble,
    RoundRobinWriter,
    SamplerEnsemble,
    SamplerWithoutReplacement,
    SliceSampler,
    SliceSamplerWithoutReplacement,
    Storage,
    StorageCheckpointerBase,
    StorageEnsemble,
    StorageEnsembleCheckpointer,
    TED2Flat,
    TED2Nested,
    TensorDictMaxValueWriter,
    TensorDictPrioritizedReplayBuffer,
    TensorDictReplayBuffer,
    TensorDictRoundRobinWriter,
    TensorStorage,
    TensorStorageCheckpointer,
    Writer,
    WriterEnsemble,
)
from .rlhf import (
    AdaptiveKLController,
    ConstantKLController,
    create_infinite_iterator,
    get_dataloader,
    PairwiseDataset,
    PromptData,
    PromptTensorDictTokenizer,
    RewardData,
    RolloutFromModel,
    TensorDictTokenizer,
    TokenizedDatasetLoader,
)
from .tensor_specs import (
    Binary,
    BinaryDiscreteTensorSpec,
    Bounded,
    BoundedTensorSpec,
    Categorical,
    Composite,
    CompositeSpec,
    DEVICE_TYPING,
    DiscreteTensorSpec,
    LazyStackedCompositeSpec,
    LazyStackedTensorSpec,
    MultiCategorical,
    MultiDiscreteTensorSpec,
    MultiOneHot,
    MultiOneHotDiscreteTensorSpec,
    NonTensor,
    NonTensorSpec,
    OneHot,
    OneHotDiscreteTensorSpec,
    Stacked,
    StackedComposite,
    TensorSpec,
    Unbounded,
    UnboundedContinuous,
    UnboundedContinuousTensorSpec,
    UnboundedDiscrete,
    UnboundedDiscreteTensorSpec,
)
from .utils import check_no_exclusive_keys, consolidate_spec, contains_lazy_spec
