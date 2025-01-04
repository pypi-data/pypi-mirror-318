#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* nepview.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcnep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepview_ NEPVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepview_ nepview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepviewfromoptions_ NEPVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepviewfromoptions_ nepviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepconvergedreasonview_ NEPCONVERGEDREASONVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepconvergedreasonview_ nepconvergedreasonview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepconvergedreasonviewfromoptions_ NEPCONVERGEDREASONVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepconvergedreasonviewfromoptions_ nepconvergedreasonviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define neperrorview_ NEPERRORVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define neperrorview_ neperrorview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define neperrorviewfromoptions_ NEPERRORVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define neperrorviewfromoptions_ neperrorviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepvaluesview_ NEPVALUESVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepvaluesview_ nepvaluesview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepvaluesviewfromoptions_ NEPVALUESVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepvaluesviewfromoptions_ nepvaluesviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepvectorsview_ NEPVECTORSVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepvectorsview_ nepvectorsview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepvectorsviewfromoptions_ NEPVECTORSVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepvectorsviewfromoptions_ nepvectorsviewfromoptions
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepview_(NEP nep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = NEPView(
	(NEP)PetscToPointer((nep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  nepviewfromoptions_(NEP nep,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = NEPViewFromOptions(
	(NEP)PetscToPointer((nep) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  nepconvergedreasonview_(NEP nep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = NEPConvergedReasonView(
	(NEP)PetscToPointer((nep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  nepconvergedreasonviewfromoptions_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPConvergedReasonViewFromOptions(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  neperrorview_(NEP nep,NEPErrorType *etype,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = NEPErrorView(
	(NEP)PetscToPointer((nep) ),*etype,PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  neperrorviewfromoptions_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPErrorViewFromOptions(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  nepvaluesview_(NEP nep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = NEPValuesView(
	(NEP)PetscToPointer((nep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  nepvaluesviewfromoptions_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPValuesViewFromOptions(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  nepvectorsview_(NEP nep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = NEPVectorsView(
	(NEP)PetscToPointer((nep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  nepvectorsviewfromoptions_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPVectorsViewFromOptions(
	(NEP)PetscToPointer((nep) ));
}
#if defined(__cplusplus)
}
#endif
