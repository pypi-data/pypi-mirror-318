def train_epoch(model, dl, nin, criterions, criterionws=None, optimizer=None, scheduler=None, epoch=None, logf='stdout', device='cuda:0', **kwargs):
    r"""train one epoch

    Parameters
    ----------
    model : Module
        an instance of torch.nn.Module
    dl : DataLoader
        the dataloader for training
    nin : int
        the number of input tensors
    criterions : list or tuple
        list of loss function, e.g. [[output_target_pair1_lossf1, output_target_pair1_lossf2], [output_target_pair2_lossf1, output_target_pair2_lossf2], ...]
    criterionws : list or tuple
        list of float loss weight, e.g. [[w11, w12], [w21, w22]]
    optimizer : Optimizer or None
        an instance of torch.optim.Optimizer, default is :obj:`None`, 
        which means ``th.optim.Adam(model.parameters(), lr=0.001)``
    scheduler : LrScheduler or None
        an instance of torch.optim.LrScheduler, default is :obj:`None`, 
        which means using fixed learning rate
    epoch : int
        epoch index
    logf : str or object, optional
        IO for print log, file object or ``'stdout'`` (default)
    device : str, optional
        device for training, by default ``'cuda:0'``
    kwargs :
        other forward args

    see also :func:`~torchbox.optim.solver.valid_epoch`, :func:`~torchbox.optim.solver.test_epoch`, :func:`~torchbox.optim.save_load.save_model`, :func:`~torchbox.optim.save_load.load_model`.
        
    """

def valid_epoch(model, dl, nin, criterions, criterionws=None, epoch=None, logf='stdout', device='cuda:0', **kwargs):
    r"""valid one epoch

    Parameters
    ----------
    model : function handle
        an instance of torch.nn.Module
    dl : dataloder
        the validation dataloader
    nin : int
        the number of input tensors
    criterions : list or tuple
        list of loss function, e.g. [[output_target_pair1_lossf1, output_target_pair1_lossf2], [output_target_pair2_lossf1, output_target_pair2_lossf2], ...]
    criterionws : list or tuple
        list of float loss weight, e.g. [[w11, w12], [w21, w22]]
    epoch : int
        epoch index,  default is None
    logf : str or object, optional
        IO for print log, file object or ``'stdout'`` (default)
    device : str, optional
        device for validation, by default ``'cuda:0'``
    kwargs :
        other forward args

    see also :func:`~torchbox.optim.solver.train_epoch`, :func:`~torchbox.optim.solver.test_epoch`, :func:`~torchbox.optim.save_load.save_model`, :func:`~torchbox.optim.save_load.load_model`.

    """

def test_epoch(model, dl, nin, criterions, criterionws=None, epoch=None, logf='stdout', device='cuda:0', **kwargs):
    """Test one epoch

    Parameters
    ----------
    model : function handle
        an instance of torch.nn.Module
    dl : dataloder
        the testing dataloader
    nin : int
        the number of input tensors
    criterions : list or tuple
        list of loss function, e.g. [[output_target_pair1_lossf1, output_target_pair1_lossf2], [output_target_pair2_lossf1, output_target_pair2_lossf2], ...]
    criterionws : list or tuple
        list of float loss weight, e.g. [[w11, w12], [w21, w22]]
    epoch : int or None
        epoch index,  default is None
    logf : str or object, optional
        IO for print log, file object or ``'stdout'`` (default)
    device : str, optional
        device for testing, by default ``'cuda:0'``
    kwargs :
        other forward args

    see also :func:`~torchbox.optim.solver.train_epoch`, :func:`~torchbox.optim.solver.valid_epoch`, :func:`~torchbox.optim.save_load.save_model`, :func:`~torchbox.optim.save_load.load_model`.

    """

def demo_epoch(model, data, bs, logf='stdout', device='cuda:0', **kwargs):
    """Test one epoch

    Parameters
    ----------
    model : function handle
        an instance of torch.nn.Module
    data : tensor or list of tensors
        the data of network inputs
    bs : int
        batch size
    logf : str or object, optional
        IO for print log, file object or ``'stdout'`` (default)
    device : str, optional
        device for testing, by default ``'cuda:0'``
    kwargs :
        other forward args

    see also :func:`~torchbox.optim.solver.train_epoch`, :func:`~torchbox.optim.solver.valid_epoch`, :func:`~torchbox.optim.save_load.save_model`, :func:`~torchbox.optim.save_load.load_model`.

    """


