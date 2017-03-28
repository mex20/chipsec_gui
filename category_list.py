# -*- coding: utf-8 -*-
categories = [
    {
        'name': u'Test of Variables UEFI',
        'info': u"""UEFI, in view UEFI, the Latest protection test variables 
        And verify that these variables have certain permissions.""",
        'modules': [
            'common.uefi.access_uefispc',
        ]
    },
    {
        'name': u'Vulnerability scanning Password BIOS / HDD via keyboard in BIOS',
        'info': u'',
        'modules': [
            '‫‪',
        ]
    },
    {
        'name': u"""Vulnerability scanning pre-boot password (Pre-Boot) in the BIOS keyboard buffer""",
        'info': u'',
        'modules': [
            '‫‪'
        ]
    },
    {
        'name': u"""Make sure to lock the settings for the event by SMI""",
        'info': u'',
        'modules': [
            'common.bios_smi',
        ]
    },
    {
        'name': u'Examine the mechanisms of protection from the BIOS in flash',
        'info': u"""In a flash, BIOS can be protected through the system management mode
         And in the controller settings via SPI.
         For example, for this test and the second mechanism is the use configuration
         SPI controller will pass successfully, you need to register P0 to P4 related
         SPI is the period of protection, cover all areas of the BIOS. If data
         Other important as NVRAM may not cover that area is vulnerable and
         Be attacked.""",
        'modules': [
            '‫‪',
        ]
    },
    {
        'name': u'SMRR Test Settings',
        'info': u"""System Management Mode Registers""",
        'modules': [
            'common.smrr',
        ]
    },
    {
        'name': u'SPI Controller settings',
        'info': u"""Which includes a review of PR0-PR4 protected sufferings locked up
         Reset which if not locked, you must re-program the registers are""",
        'modules': [
            'common.spi_lock',
        ]
    },
    {
        'name': u'Check the SMI handler to detect vulnerabilities related to addressing',
        'info': u'',
        'modules': [
            'tools.smm.smm_ptr'
        ]
    },
    {
        'name': u'Evaluation tests relating to the protection DMA',
        'info': u"""The test settings and lock the set ranges SMRAM review
        And the accuracy ensures protection against DMA. \ N In fact,
        As SMRAM should Fazzari that the CPU run Nrn
        Be safe, requires hardware that have direct access to the DRAM
        Are) DMA (also to be protected. In fact, protection of the DMA, through program
        SMRAM protected area is set and if the BIOS is not set correctly and
        These settings are not locked, so malware can reset settings
        Program and SMRAM area are at risk of DMA access. And thus
        Allow manipulation of memory that must be protected.""",
        'modules': [
            'modules.smm_dma'
        ]
    },
    {
        'name': u'Check the contents of UEFI firmware ROM',
        'info': u"""By comparison with the blacklist already on file for it
         defined. And if Image files are unhealthy or have had
         This is their signature definition files to compare and consider the validity of the current Image
         To be""",
        'modules': [
            '‫‪'
        ]
    },
    {
        'name': u'SPI flash reading and writing test',
        'info': u"""Image files are created when an SPI flash reading,
         The tool has been developed can pass this Image and its various sectors
         Includes variables, files and ... revealed.""",
        'modules': [
            'utilcmd.decode_cmd',
            'utilcmd.uefi_cmd'
        ]
    },
    {
        'name': u'The ability to access physical memory',
        'info': u'',
        'modules': [
            '‫‪'
        ]
    },
    {
        'name': u'ACPI tables and manipulate their access to',
        'info': u'',
        'modules': [
            '‫‪'
        ]
    }
]
